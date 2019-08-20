import requests
import datetime
from numpy import random

URLS = ("temperatura-pozo", "ph-pozo", "oxigeno-disuelto") # nombre de la parte de las URL donde se encuentra la API
for uri in URLS:
    url = "http://127.0.0.1:8080/piscicultura/"

    #valores aleatorios para registrar en nuestro pozo
    fecha = datetime.datetime.now()
    valor = random.randn()*20

    pyload = {
        "fecha": fecha,
        "valor": valor,
        "pozo": 1 # es uno porque es el id del primer registro que hicimos
    }

    r = requests.post(url+uri, data=pyload) # metodo POST para enviar nuestros datos a la base de datos
    print(r.text)
    print(r.status_code)
    r.close()