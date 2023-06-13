import yaml
import os
import json
import joblib
import numpy as np

params_path = 'params.yaml'
schema_path = os.path.join('prediction_service', 'schema_in.json')

class NotInRange(Exception):
    def __init__ (self, message = "values are not in range"):
        self.message = message
        super().__init__(self.message)

class NotInCols(Exception):
    def __init__ (self, message = "Not in Columns"):
        self.message = message
        super().__init__(self.message)


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir = config['webapp_model_dir']
    model = joblib.load(model_dir) # load the model
    print(data)
    prediction = model.predict(data)
    return round(prediction[0], 3)

    # try:
    #     if 3 <= prediction <= 8:
    #         return prediction
        
    #     else:
    #         return NotInRange
    # except NotInRange:
    #     return 'Unexpected Results'
     
def get_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def validate_input(dict_request):

    def _validate_cols(col):
        schema =  get_schema(schema_path)
        actual_cols = schema.keys()
        if col not in actual_cols:
            print(actual_cols)
            print(col)
            raise NotInCols
        
    def _validate_values(col, val):
        schema = get_schema(schema_path)
        
        if not(schema[col]['min'] <= float(dict_request[col]) <= schema[col]['max']):
            raise NotInRange

    for col, val in dict_request.items():
        _validate_cols(col)
        _validate_values(col, val)

    return True

def form_response(dict_response):
    if validate_input(dict_response):
        data = dict_response.values()
        data = [list(map(float, data))]
        # print(data)
        response = predict(data)

        return response

def api_response(dict_request):
    try:
        if validate_input(dict_request):
            data = np.array([list(dict_request.json.values())])
            response = predict(data[0])
            response = {'response': response}
            return response
    
    except Exception as e:
        response = {'the expexted range': get_schema(schema_path), 'response': str(e)}
        return response