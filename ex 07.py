qtd_50anos = 0
qtd_idade1020 = 0
qtd_peso40 = 0
somaAlt = 0
for i in range(6):
    idade = int(input(f'Informe a idade da {i+1} pessoa: '))
    altura = float(input(f'Informe a altura da {i+1} pessoa: '))
    peso = float(input(f'Informe o peso da {i+1} pessoa: '))

    if idade > 50:
        qtd_50anos += 1
        
    if idade >= 10 and idade <= 20:
        qtd_idade1020 += 1
        somaAlt += altura
            
    if peso < 40:
        qtd_peso40 += 1

print(f'Quantidade de pessoas com mais de 50 anos: {qtd_50anos}')

if qtd_idade1020 == 0:
    print('Nenhuma pessoa com idade entre 10 e 20 anos foi inserida')
else:
    media = somaAlt / qtd_idade1020
    print(f'Média de alturas das pessoas com idade entre 10 e 20 anos: {media:.2f}')
if qtd_peso40 == 0:
    print('Nenhuma pessoa com peso inferior a 40kg foi inserido')
else:
    porcentagem = (qtd_peso40/3)*100
    print(f'Porcentagem de pessoas com peso inferior a 40kg entre todas as pessoas: {porcentagem:.2f}%')

