'''
Considere a lista abaixo e escreva um programa que mostre na tela o seu maior número.

'''

lista=[497, 186, 66, 198, 204, 339, 738, 743, 
       -80, 36, 887, 645, 312, 760, 574, 439, 
       164, 873, 125, 871, 901, 561, 5, -65, 
       -66, -51, 522, 306, -79, 577, 268, 240, 
       183, 217, 729, 202, 483, 464, 281, 6, 
       -44, 110, 670, 749, 846, 903, 15, 265, 
       596, -3, 534, -42, 528, 582, 552, 254, 
       780, 326, 816, -7, 859, 234, 898, 355, 
       706, 576, 968, 349, 649, 522, 466, 353, 
       940, 41, 141, 946, 317, 346, 256, 326, 
       546, 473, 270, 22, 102, 504, 421, 87, 
       570, 143, 519, 292, 382, 744, 525, 658, 
       725, 477, 413]

maior = max(lista)
print(maior)


#ouuuuuu

max_=lista[0]
for num in lista:
    if num>max_:
        max_=num
print(max_)