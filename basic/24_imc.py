print('Cálculo do IMC')
altura=float(input('Insira sua altura : \n'))
peso=float(input('Insira seu peso : \n'))
imc=peso/(altura*altura)  #poderíamos fazer peso/altura**2
print('Processando seus dados...')
if imc<17:
    print('Muito abaixo do peso.')
elif 17<=imc<18.5:
    print('Abaixo do peso.')
elif 18.5<=imc<25:
    print('Peso normal.')
elif 25<=imc<30:
    print('Acima do peso.')
elif 30<=imc<35:
    print('Obesidade Grau I.')
elif 35<=imc<40:
    print('Obesidade Grau II (severa).')
else:
    print('Obesidade Grau III (mórbida).')