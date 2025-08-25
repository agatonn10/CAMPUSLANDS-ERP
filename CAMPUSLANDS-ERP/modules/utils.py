import json

BASE_DATOS = "CAMPUSLANDS-ERP/data/database.json"

def load_data():
    try:
        with open(BASE_DATOS, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def save_data(data):
    with open(BASE_DATOS, "w") as file:
        json.dump(data, file, indent=4)