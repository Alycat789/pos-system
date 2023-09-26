import os
import json
ROOT_DIR = os.path.dirname(__file__)

def make_path(file_name):
    return os.path.join(ROOT_DIR, file_name)

def read_json(file_name):
    """reads json file"""
    with open(make_path(file_name)) as f:
        return json.load(f)
    
def load_json(file_name, data):
    """opens/loads data into json file"""
    with open(make_path(file_name), 'w') as f:
        json.dump(data, f, indent= 4)