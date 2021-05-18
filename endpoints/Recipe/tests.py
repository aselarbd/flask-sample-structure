import requests

BASE_URI = "http://127.0.0.1:5000/"

resp = requests.get(BASE_URI + "/recipe")
print(resp.json())
