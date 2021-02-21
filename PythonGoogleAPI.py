#https://developers.google.com/maps/

import urllib.request, urllib.error, urllib.parse #Esta librería trabaja con urls
import json 

serviceurl = 'http://maps.google.com/maps/api/geocode/json?'

while True:
    address = input('Pon el lugar a buscar: ')
    if len(address)<1: 
        break
    url = serviceurl + urllib.parse.urlencode(
        {'address': address})
    print('El url compuesto es: ',url)
    uh= urllib.request.urlopen(url) #se hace la llamada con la URL
    data=uh.read().decode() #se leen los datos, pero se tiene que hacer un decode porque viene desde afuera de internet
    print('Se encontraron: ', len(data), 'caracteres')
    try:
        js = json.loads(data) #se tratan de cargar los datos en json
    except: 
        js = None
    if not js or 'status' not in js or ['status'] != 'OK': #checamos si tiene la informacion del ok status
        print('=========Falla en traer la informacion :(') 
        print(data) #de todos modos hacemos print de la informacionn
        continue
    print(json.dumps(js,indent=4)) #imprimimos la informacion del json con una identacion de 4 tabs
    lat = js['results'][0]['geometry']['location']['lat'] #latitud
    lng = js['results'][0]['geometry']['location']['lng'] #longitud
    print('latitud: ', lat, 'longitud: ', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    