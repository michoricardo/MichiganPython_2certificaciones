#datos ejemplo para ejercicio:    http://py4e-data.dr-chuck.net/comments_42.json
#datos reales para ejercicio:     http://py4e-data.dr-chuck.net/comments_732971.json
import urllib
import urllib.request
import json
sumaloka = 0
cuentaloka =0
while True:
    url = input('Pon el lugar a buscar: ')
    if len(url)<1: 
        break
    #url = urllib.parse.urlencode({'address': address})
    print('El url a buscar es: ',url)
    uh= urllib.request.urlopen(url) #se hace la llamada con la URL
    data=uh.read().decode() #se leen los datos, pero se tiene que hacer un decode porque viene desde afuera de internet
    print('Se encontraron: ', len(data), 'caracteres')
    #print(data)
    datajson=json.loads(data)
    for x in datajson['comments']:
        actual_name=(x["name"])
        actual_count=int(x["count"])
        print('Nombre iteracion actual :' ,actual_name)
        print('Cuenta iteracion actual :' ,actual_count)
        sumaloka = sumaloka + actual_count
        cuentaloka += 1
    break
print('La cuenta total es: ',cuentaloka)
print('La suma total es: ', sumaloka)
    