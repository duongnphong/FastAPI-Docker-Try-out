import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/greet}")
def greet_name(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/catfact")
def cat_fact():

    response = requests.get("https://meowfacts.herokuapp.com/")
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, port=12345, host="0.0.0.0")
