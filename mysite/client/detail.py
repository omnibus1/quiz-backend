import requests

endpoint="http://127.0.0.1:8000/api/quizes/1123/"

response=requests.get(endpoint)
print(response.text)
print(f'status code: {response.status_code}')