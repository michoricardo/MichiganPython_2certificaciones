#Los metodos de la clase str
name='RiCaRdO'
print(name.lower())
print(name.upper())

if 'RI' in name:
    print('si estoy!')
else:
    print('No estoyyy')

posicion = name.find('d')
print(posicion)

replace=name.replace('R','F')
print(replace)

stringCespacios= '    Richi  ' # 4 espacios antes y 2 despues
print(stringCespacios.rstrip()) #quita los 4 antes
print(stringCespacios.strip()) #quita los 2 despues

data = 'From ricardo@nevillegoddard.com received at Sat may 5th'
arrobaPos= data.find('@')
hostPos=data.find('.com')
print(hostPos)
host=data[arrobaPos:31]
print(host)