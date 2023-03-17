import requests
from data_in import data_in

Url= 'http://127.0.0.1:5000/predict'
headers = {'Content-type':'application/json'}
data={"input": data_in}

r= requests.get(Url, headers=headers, json=data)

print(r.json())