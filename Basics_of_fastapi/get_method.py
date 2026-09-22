from fastapi import FastAPI
import json

app = FastAPI()


def load_data():
    with open('patients.json', 'r') as f:
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