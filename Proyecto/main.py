import requests

url= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"

r= requests.get(url)
edd= r.json()
