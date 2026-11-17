profile = {
    "name": "민수",
    "skills": ["Python", "HTML"],
    "active": True,
}

print(profile["name"]) #민수
print(profile["skills"][0]) #python
print(len(profile["skills"])) #2
print(profile["active"]) #true

profile["name"] = "지수" #지수 출력
profile["skills"].append("SQL") #sql이 들어감 dic, skills에
print(profile["name"]) #민수, 지수
print(profile["skills"]) #python, html, sql
print(len(profile["skills"])) #3