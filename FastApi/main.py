from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/create_user/")
def create_user(name: str, age: int):
    return {"name": name, "age": age}