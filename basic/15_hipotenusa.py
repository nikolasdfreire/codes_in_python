from math import hypot
 
cateto_a=float(input('Digite o Cateto Adjacente: '))
cateto_o=float(input('Digite o Cateto Oposto: '))
 
hipotenusa1=(cateto_a**2+cateto_o**2)**(1/2)  #forma de cálculo 1
hipotenusa2=hypot(cateto_a,cateto_o)  #forma de cálculo 2
 
print(f'Hipotenusa: {hipotenusa1}')
print(f'Hipotenusa: {hipotenusa2}')
    