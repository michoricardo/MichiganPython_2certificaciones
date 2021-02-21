def do_math(a, b, kind='add'):
  if (kind=='add'):
    return a+b
  else:
    return a-b

do_math(1, 2)

x = 'Dr. Christopher Brooks'

print(x[4:])
print(x[4:15])

nombre= 'Ricardo García Reyes'
nombremochado = nombre.split(' ')[-1]
print(nombremochado) #imprime Reyes