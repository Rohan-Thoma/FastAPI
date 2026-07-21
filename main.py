from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': "Hello world" }

@app.get("/ about")
def about():
    return {"This is the dummy to test fastapi app"}