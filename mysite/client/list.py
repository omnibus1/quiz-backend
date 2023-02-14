import requests

endpoint="http://127.0.0.1:8000/api/quizes/"

response=requests.get(endpoint)
print(response.json())
print(f'status code: {response.status_code}')