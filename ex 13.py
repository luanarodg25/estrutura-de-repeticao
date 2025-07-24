cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
somap1 = 0
somap2 = 0
somap3 = 0
somap4 = 0
for i in range (15):
    idade = int(input(f'Idade {i+1}° pessoa:'))
    peso = float(input(f'Peso {i+1}° pessoa: '))
    print('-'*14)

    if idade >=1 and idade <= 10:
        cont1 +=1
        somap1 += peso
    elif idade >= 11 and idade <= 20:
        cont2 += 1
        somap2 += peso
    elif idade >= 21 and idade <= 30:
        cont3 += 1
        somap3 += peso
    else:
        cont4 += 1
        somap4 += peso

if cont1 == 0:
    print('Nenhuma pessoa entre 1 a 10 anos foi inserida')
else:
    media1 = somap1/cont1
    print(f'A média dos pesos na primeira faixa etária é {media1:.2f}')
if cont2 == 0:
    print('Nenhuma pessoa entre 11 a 20 anos foi inserida')
else:
    media2 = somap2/cont2
    print(f'A média dos pesos na segunda faixa etária é {media2:.2f}')
if cont3 == 0:
    print('Nenhuma pessoa entre 21 a 30 anos foi inserida')
else:
    media3 = somap3/cont3
    print(f'A média dos pesos na terceira faixa etária é {media3:.2f}')
if cont4 == 0:
    print('Nenhuma pessoa acima de 31 anos foi inserida')
else:
    media4 = somap4/cont4
    print(f'A média dos pesos na quarta faixa etária é {media4:.2f}')



    
