import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#NO TENGO API KEY DEL GUGUL
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignora errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Escribe el lugar para encontrar sus datos: ')
    if len(address) < 1: break
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    #URL TRABAJADO
    print('El url trabajado es: ', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Se encontraron ', len(data), 'caracteres')
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Falla al recibir los datos====')
        print(data)
        continue
    print(json.dumps(js, indent=4))
    idDeLugar= js['results'][0]['place_id']
    lat = js['results'][0]['geometry']['location']['lat'] #latitud
    lng = js['results'][0]['geometry']['location']['lng'] #latitud
    formateada=js['results'][0]['formatted_address']
    print('El id de lugar es: ', idDeLugar)
    print('Con latitud ',lat, 'y longitud ',lng)
    print('Su direccion bonita es: ',formateada)