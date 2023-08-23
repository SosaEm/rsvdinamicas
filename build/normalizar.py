import requests
import urllib
import csv
import json

API_BASE_URL = "https://apis.datos.gob.ar/georef/api/"

def get_similar_bulk(direcciones):
    """Normaliza una lista de nombres de alguna de las entidades geográficas."""

    # realiza consulta a la API
    endpoint = "direcciones"
    data = {
        "direcciones": [
            {"direccion": direccion["direccion"], "departamento": direccion["departamento"], "provincia": "buenos aires", "localidad": direccion["localidad"], "orden": "id","campos": "ubicacion.lat, ubicacion.lon", "max": "1"}
            for direccion in direcciones
    ]}
    url = API_BASE_URL + endpoint
    results = requests.post(
        url, json=data, headers={"Content-Type": "application/json"}
    ).json()

    # convierte a una lista de "resultado más probable" o "vacío" cuando no hay
    parsed_results = [
        single_result[endpoint][0] if single_result[endpoint] else {}
        for single_result in results["resultados"]
    ]

    return parsed_results

#direcciones = get_similar_bulk([{"direccion": "republica argentina 6105", "localidad": "burzaco", "departamento": "almirante brown"}])
#print(direcciones)

f = open(r'C:\Users\esosa\Desktop\Nominatim\rsvdinamicas\informes\personal.json')
data=json.load(f)
json_str = json.dumps(data)
resp = json.loads(json_str) 

with open('informes\personal.json', 'r', encoding='utf-8') as json_file:
    for x in resp:
        provincias = get_similar_bulk([{"direccion":x["direccion"] + " " + x["altura"], "departamento": x["partido"], "localidad": x["localidad"]}])
        with open('informes/normalizar.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(["{};{};{};{};{};{}" .format(x['record_id'],x["hospital"],x["fecha_ingreso"],provincias,x["uti"],x["dx_egreso"])])

