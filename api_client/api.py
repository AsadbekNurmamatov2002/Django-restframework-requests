import requests


endpoint="http://127.0.0.1:8000/api/"
r=requests.get(endpoint, json={"ismmm":"OLIMbek"})#api -> method
# print(r.text)
print(r.json())
print(r.json())
print(r.status_code)
