from email import message
import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={"title" : "Hello World"})

"""Test POST Respon Failing"""
# get_response = requests.post(endpoint, json={"title" : None, "content" : "Hello World"}) 

"""Request GET Method"""
# get_response = requests.get(endpoint, json={"query" : "Hello World"})

#print(get_response.text)
print(get_response.json())
#print(get_response.status_code)
 