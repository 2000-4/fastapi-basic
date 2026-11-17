# BASE_KM = 3 # 전역변수 이 코드 어디에서든 사용 가능하다

# def greeting(name): # name은 지역변수 // 매개변수 이 함수 안에서만 사용 가능하다
#     return {"message": name + "님, 안녕하세요"}


# print(greeting("민수"))
# print(greeting("지수")["message"])
# print(["사과", "바나나"][0])

def make_message(name):
    return name + "님, 안녕하세요"


def show_message(name):
    print(name + "님, 안녕하세요")


message = make_message("민수")
print(message)
print(message + "!")
result = show_message("지수")
print(result)