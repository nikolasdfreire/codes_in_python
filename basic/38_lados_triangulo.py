lado1 = float(input('Digite o lado 1 do quadrado: '))
lado2 = float(input('Digite o lado 2 do quadrado: '))
lado3 = float(input('Digite o lado 3 do quadrado: '))

if lado1 == lado2 == lado3:
    print('O tringulo é equilatero')
elif lado1 != lado2 or lado2 != lado3 or lado3 != lado1:
    print('O triangulo é escaleno')
else:
    print('O triangulo é isóceles')
