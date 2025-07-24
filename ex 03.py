qtd1 = 0
qtd2 = 0 
qtd3 = 0 
qtd4 = 0 
qtd5 = 0 

for i in range(1,9):
    idade = int(input(f'Informe a idade da {i}° pessoa: '))

    if idade <= 15:
        qtd1 += 1
    elif idade >= 16 and idade <= 30:
        qtd2 += 1
    elif idade >= 31 and idade <= 45:
        qtd3 += 1
    elif idade >=46 and idade <= 60:
        qtd4 += 1
    else:
        qtd5 += 1
        
total = qtd1 + qtd2 + qtd3 + qtd4 + qtd5
porcentagem1 = (qtd1/total)*100
porcentagem5 = (qtd5/total)*100


if total == 0:
    print('Nenhuma pessoa cadastrada')
    print('A porcentagem de pessoas na primeira faixa etária é 0%')
    print('A porcentagem de pessoas na última faixa etária é 0%')
else:
    porcentagem1 = (qtd1 / total) * 100
    porcentagem5 = (qtd5 / total) * 100

    print('Quantidade faixa 1: ', qtd1)
    print('Quantidade faixa 2: ', qtd2)
    print('Quantidade faixa 3: ', qtd3)
    print('Quantidade faixa 4: ', qtd4)
    print('Quantidade faixa 5: ', qtd5)
    print('-' * 10)
    print(f'A porcentagem de pessoas na primeira faixa etária é {porcentagem1:.2f}%')
    print(f'A porcentagem de pessoas na última faixa etária é {porcentagem5:.2f}%')
