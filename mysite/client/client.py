import requests

endpoint="http://127.0.0.1:8000/api/"

response=requests.post(endpoint,json={"title":"Hello world","content":"some shit","price":"123"})
print(response.text)
print(f'status code: {response.status_code}')