hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter rate:')
r= float(rate)

#Si horas mayor a 40, entonces 
if h> 40:
    extras=h-40
    normal=40
    extra_rate=r*1.5
    pay=((normal*r)+(extras*extra_rate))
print(pay)
 
    