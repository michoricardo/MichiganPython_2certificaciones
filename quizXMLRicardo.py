import urllib
import urllib.request
import xml.etree.ElementTree as ET
url = input("Pon el link a evaluar: ")
#uh = urllib.urlopen(url)
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

lista = tree.findall('comments/comment') #encuentra del tag comments que es el grande, todos los hijitos comment
print('Tienes : ', len(lista), 'Tags')
count=0
sum=0
for comentario in lista:
    print('Comentario actual de numero: ', comentario.find('count').text)
    x=comentario.find('count').text
    x=int(x)
    count=count+1
    sum=sum+x
print('cuenta total: ', count)
print('Suma de esos numeros en los tags: ',sum)

