## read params
## process the data
## return data frame

import yaml
import pandas as pd
import argparse # to parse the arguments that we are getting from the command prompt

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = config['data_source']['s3_source']
    df = pd.read_csv(data_path, delimiter= '\s+', header=None)
    print(df.head())
    return df

if __name__ == "__main__":

    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
    # get_data = (config_path )

