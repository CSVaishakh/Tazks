import json,os

def load_json(file_path : str) -> dict:
    if os.path.exists(file_path):
        with open(file_path,'r')as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_json(data : dict, file_path : str):
    with open(file_path,'w') as f:
        json.dump(data,f,indent=4)
