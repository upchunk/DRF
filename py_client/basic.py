import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "localhost:8000"

get_response = requests.get(endpoint, json={"query" : "Hello World"})
print(get_response.text)

print(get_response.json())
print(get_response.status_code)
