from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def home():
    return {"message" : "pong"}


@app.get("/status")
def home():
    return {"running" : True}