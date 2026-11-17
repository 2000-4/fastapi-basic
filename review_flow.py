def build_greetings(names):
    messages = []
    for name in names:
        if name != "":
            messages.append(name + "님, 안녕하세요")
    return {"count": len(messages), "items": messages}


result = build_greetings(["민수", "", "지수"])
print(result) #민수, 지수
print(build_greetings([])) # 

assert result["count"] == 2 #
assert result["items"] == ["민수님, 안녕하세요", "지수님, 안녕하세요"]
assert build_greetings([]) == {"count": 0, "items": []}
print("확인 완료")