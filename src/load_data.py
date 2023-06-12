## read the data from the data source and then store it in the data/raw for the further processing

import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = ['Sno',  'BF1',    'BF2',  'Density',    'Age',  'Weight', 'Height',    'Adiposity',    'Fat_Free_Weight',  'Neck',   'Chest',   'Abdomen', 'Hip',   'Thigh',   'Knee',    'Ankle',    'biceps',   'Forearm', 'Wrist']
    df.columns = new_cols
    
    df['BF'] = df['BF1'] + df['BF2']
    df['BF'] = df['BF']/2

    df = df.drop(['Adiposity','Fat_Free_Weight','BF1','BF2','Sno','Density'],axis = 1)
    raw_data_path = config['load_data']['raw_dataset_csv']
    print(raw_data_path)
    df.to_csv(raw_data_path, sep = ",", index=False, header=['Age',  'Weight', 'Height',  'Neck',   'Chest',   'Abdomen', 'Hip',   'Thigh',   'Knee',    'Ankle',    'biceps',   'Forearm', 'Wrist', 'BF'])

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = load_and_save(config_path=parsed_args.config)
