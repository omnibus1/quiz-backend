import requests

endpoint="http://127.0.0.1:8000/api/test/"

response=requests.get(endpoint,json={"quiz name":"fizyka 1"})

print(response.text)
print(f'status code: {response.status_code}')