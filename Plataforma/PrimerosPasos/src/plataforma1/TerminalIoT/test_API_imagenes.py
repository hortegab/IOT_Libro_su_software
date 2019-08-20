import requests

files = {'imagen': open("IMG_0247.JPG", "rb")}
pyload = {'region': 1}
url = "http://127.0.0.1:8080/app_prueba/album-imagenes"
r = requests.post(url, data=pyload, files=files)
print(r.text)
print(r.status_code)
r.close()