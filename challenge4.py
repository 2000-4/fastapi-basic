from fastapi import FastAPI

app = FastAPI()

@app.get("/sum/{left}/{right}")
def sum(left: int, right: int):
    return {"result" : left * right}