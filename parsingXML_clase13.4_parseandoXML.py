import xml.etree.ElementTree as ET
data = '''<person>
<name>Micky</name>
<phone type="int1">
+8441111111
</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('NAME: ', tree.find('name').text)
print('ATTR: ', tree.find('email').get('hide'))

input= '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Richi</name>
        </user>
        <user x="3">
            <id>009</id>
            <name>Fabiola</name>
        </user>
    </users>
</stuff>'''
stuff = ET.fromstring(input)
lista = stuff.findall('users/user') #encuentra todos los user (osea hijos del tag users)
print('Tienes : ', len(lista), 'Usuarios')
for item in lista:
    print('Nombre: ', item.find('name').text)
    print('ID: ', item.find('id').text)
    print('Atributo: ', item.get("x"))
