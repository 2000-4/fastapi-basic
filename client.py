import requests

response = requests.post("http://127.0.0.1:8000/count", json={"items" : ["사과" , "바나나"]})
print(response.status_code)
print(response.json())

response = requests.post("http://127.0.0.1:8000/echo", json={"text": "안녕"})
print(response.status_code)
print(response.json())