from fastapi import FastAPI, Path, HTTPException
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
        data = json.load(f)
    
    return data 

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient in the Database", example="P001") ):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="patient not found")
