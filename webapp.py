import requests


url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.request("GET",url)

print(response.json()['title'])