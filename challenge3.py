from fastapi import FastAPI

app = FastAPI()

@app.get("/about")
def about():
    return {"name" : "연습" , "version" : 1 , "List" : ["Python", "JavaScript"]}