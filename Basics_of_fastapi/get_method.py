from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "patients.json"


def load_data():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {'message':'Patient management system api'}

@app.get("/about")
def about():
    return {'message':'A fully functional api to manage your patient records'}

# create a new endpoint

@app.get("/view")  # It will give all the patients data
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')    # This is our route.
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB',example='P001')):    # This is our function.

    # Now write the logic of function,(load all the patient).
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {'error':'patient not found'}