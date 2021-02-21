#Este está bien
print('while loop')
fruit = 'banana'
index=0
while index < len(fruit):
    print(index,fruit[index])
    index=index+1
#pero siempre un for funciona mejor
print('for loop')
for letter in fruit:
    print(letter)


#slicing avanza hasta tonde le digamos pero no incluye
complete = 'Richard'
slice1=complete[0:2] ##no incluye la posicion 2, solo 0 y 1
print(slice1)
slice2=complete[2:]
print(slice2)
