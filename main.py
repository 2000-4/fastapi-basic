from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import random


app = FastAPI()

class Item(BaseModel):
    name: str
    price: int = 1000
@app.post("/items", summary="상품 등록", tags=["실습"])
def create_item(item: Item):
    """JSON 데이터를 받아서 그대로 돌려줍니다."""
    return {"등록된_상품": item}


@app.get("/ui", include_in_schema=False)
def frontend():
    return FileResponse("index.html")


@app.get("/")
def home():
    return {"message": "ㅎㅇ", "course" : "FastAPI", "no" : "yes"}


@app.get("/health", summary="서버 온?")
def health():
    return {"status" : "ok"} # 서버가 켜져 있는지 확인


@app.get("/bye", summary="빠이")
def health():
    return {"인사" : "바이"}


@app.get("/info", summary="서버 인포")
def health():
    return {"name" : "연습 서버", "version" : 1}

@app.get("/fruits", summary="과일")
def fruits():
    return ["사과", "바나나"]

@app.get("/JSON", summary="JSON test")
def json():
    return {
  "name": "홍길동",
  "age": 30,
  "isStudent": False,
  "skills": ["JavaScript", "Python", "JSON"],
  "address": {
    "city": "서울",
    "zipcode": "04524"
  }
}

@app.get("/fruit-info", summary="과일바구니")
def fruit_info():
    fruits = ["사과", "바나나", "포도", "수박", "자몽", "용과"]
    pickedfruit = random.choice(fruits)
    return {"fruits" : pickedfruit}


@app.get("/languages", summary="언어")
def languages():
    lang = ["한국어", "English", "일본어", "러시아어", "중국어", "프랑스어"]
    pickedlang = random.choice(lang)
    return {"languages" : pickedlang}


@app.get("/numberplay/{number}", summary="곱하기 5")
def numberplay(number: int):
    """쓴 숫자에 곱하기 5를 해 줌"""
    return {"numberplay-start" : number * 5 }


@app.get("/length/{text}", summary="글자수")
def numberplay(text):
    """쓴 글자의 길이를 구해 줌"""
    return {"legnth" : len(text) }

@app.get("/greet", summary="한테 인사하기")
def greet(name : str = "민수"): # 기본값 세팅 // 민수가 기본값으로 들어오는 쿼리 스트링임을 알아야 한다
    """인사를 해 준다"""
    return {"message" : name + "님, 안녕하세요."}

@app.get("/repeat", summary="번 반복")
def repeat(word : str, count : int = 1):
    return {"text-repeat" : word * count}

@app.get("/launch", summary="오늘 점심 메뉴", tags=["음식"])
def launch():
    menus = ["라멘", "김치찌개", "돈까스", "초밥", "제육볶음", "파스타", "국밥"]
    picked = random.choice(menus)
    return {"점심메뉴": picked}


@app.post("/echo")
def echo(data : dict):
    return data

@app.post("/count")
def count(data : dict):
    # return {"count" :2}
    count = len(data["items"])
    response = {"count" : count}
    return response


    