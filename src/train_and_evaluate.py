# test and log the scores of all pur models

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet, LinearRegression
from get_data import read_params
import argparse
import joblib
import json
import mlflow
from urllib.parse import urlparse # this is to check if the server is on then it will log the data in the server 
# and in case the server is not on then it will create a folder and log all the details inside that folder


def eval_matrix(actual, pred):
    rmse = np.sqrt(mean_absolute_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)

    return rmse, mae, r2

def train_and_evaluate(config_path):

    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",", encoding='utf-8')
    test = pd.read_csv(test_data_path, sep=",", encoding='utf-8')

    print(target)

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    # ---------------- MLFLOW ------------------ #

    mlflow_config = config['mlflow_config']
    remote_server_uri = mlflow_config['remote_server_uri']

    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(mlflow_config['experiment_name'])

    with mlflow.start_run(run_name = mlflow_config['run_name']) as mlops_run:
        print('model logging starts')

        lr = joblib.load('saved_models/random_forest.joblib')
        print(test_x)

        predicted_qualities = lr.predict(test_x)
        (rmse, mae, r2) = eval_matrix(test_y, predicted_qualities)

        print("Decision Tree")
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        mlflow.log_metric('rmse', rmse)
        mlflow.log_metric('mae', mae)
        mlflow.log_metric('r2_score', r2) # these are the steps to log the data in the mlflow

        tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme

        if tracking_url_type_store != 'file':
            mlflow.sklearn.log_model(lr, 'model', registered_model_name = mlflow_config['registered_model_name'])
            # mlflow.sklearn.log_model(lr, 'model', registered_model_name = "linear regression")

        else:
            mlflow.sklearn.load_model(lr, 'model')

if __name__ == "__main__":

    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
