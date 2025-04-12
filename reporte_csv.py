import requests
import pandas as pd

url="http://127.0.0.1:8000/api/register"

response = requests.get(url)

if response.status_code == 200:
    datos= response.json()

    for registro in datos[:3]:
        print(registro)

else:
    print("Error en la solicitud", response.status_code)

df = pd.DataFrame(datos)

df.to_csv('datos_api.csv', index=False)

print("Datos generados en archivo csv datos_api.csv")