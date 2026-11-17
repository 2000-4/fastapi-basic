from fastapi import FastAPI

app = FastAPI()

@app.get("/fruit-info")
def fruit_info():
    fruits = ["사과", "바나나"]
    return {"count": len(fruits), "items": fruits, "available": True}

@app.get("/languages")
def languages() :
    return ["Python" , "JavaScript"]