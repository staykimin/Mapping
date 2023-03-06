import requests

url = "http://localhost:5000"
data = {
	"label":"Testing",
	"warna":"Testing",
	"author":"Testing",
	"long":"Testing",
	"lat":"Testing"
	}
respon = requests.post(url, data=data)
print(respon.text)