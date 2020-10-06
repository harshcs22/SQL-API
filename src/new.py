import requests

url = "http://18.222.149.196:8080/all"

payload = {}
files = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
