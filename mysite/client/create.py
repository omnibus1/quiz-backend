import requests

endpoint="http://127.0.0.1:8000/api/create/"
data={"title":"jd","content":"orka disa","price":"325"}
response=requests.post(endpoint,json=data)
print(response.json())
print(f'status code: {response.status_code}')