from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/profile")
def profile(name : str = "민수", interest : str ="파이썬"):
    return {"name": name , "interest" : interest}

@app.get("/hello/{name}")
def hello(name : str):
    return {"message" : f"{name}님, 안녕하세요"}

@app.get("/repeat")
def repeat(word : str = "안녕", count : int = 1):
    return {"text" : word * count}

@app.post("/introduce")
def introduce(data : dict):
    data = {"name" : "interest"}
    return data

@app.get("/length/{text}")
def length(text : str) :
    return len(text)