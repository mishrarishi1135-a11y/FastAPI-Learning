from fastapi import FastAPI
app = FastAPI()

@app.get("/")          # first endpoint
def home():
    return {"message": "Hello FastAPI"}

@app.get("/about")           # Second endpoint
def about():
    return {"message": "Learning FastAPI"}

# This is how we can create endpoints in fastapi.