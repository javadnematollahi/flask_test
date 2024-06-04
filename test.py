import requests

response = requests.get("http://127.0.0.1:5000/blog")
print(response.text)

response = requests.post("http://127.0.0.1:5000/blog")
print(response.text)


