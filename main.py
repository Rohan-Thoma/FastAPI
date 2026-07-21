from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def hello():
    return {'message': "Patient Management System API" }

@app.get("/about")
def about():
    return {"message" : "A fully functional API to manage your patient records"}

#Helper function to fetch all the patient records from the file in the server
def load_data():
    with open("patients.json", 'r') as f:
        data = json.loads(f)
    
    return data 

@app.get("/view")
def view():
    data = load_data()

    return data

