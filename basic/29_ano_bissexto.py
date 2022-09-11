ano=int(input('Ano : '))
if ano%400==0 or (ano%4==0 and not ano%100==0):
    print('Ano bissexto.')
else:
    print('Ano não bissexto.')