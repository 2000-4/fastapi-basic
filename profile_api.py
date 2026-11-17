from fastapi import FastAPI
from fastapi.responses import FileResponse

import requests

response = requests.post("http://127.0.0.1:8001/count", json={"items" : ["사과" , "바나나"]})
print(response.status_code)
print(response.json())

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
    data = {"message" : f"{data['name']}님은 {data['interest']}에 관심이 있습니다."}
    return data

@app.get("/length/{text}")
def length(text : str) :
    return len(text)