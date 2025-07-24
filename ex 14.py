qtd_otimo = 0
somaIdade = 0
qtd_regular = 0
qtd_bom = 0
pessoas = 15

for i in range(pessoas):
    idade = int(input(f'Informe a idade do {i+1}° espectador: '))

    while True:
        opniao = int(input(f'Informe sua opinião sobre o filme (ótimo - 3; bom - 2; regular - 1): '))
        if opniao in [1, 2, 3]:
            break 
        else:
            print('Opinião inválida! Digite apenas 1, 2 ou 3.')

    if opniao == 3:
        somaIdade += idade
        qtd_otimo += 1

    elif opniao == 1:
        qtd_regular += 1

    elif opniao == 2:
        qtd_bom += 1

if qtd_otimo == 0:
    print('Nenhuma pessoa respondeu como ótimo')
else:
    media = somaIdade / qtd_otimo
    print(f'A média das idades das pessoas que responderam ótimo foi {media:.2f}')

print('A quantidade de pessoas que responderam regular é', qtd_regular)

if qtd_bom == 0:
    print('Nenhuma pessoa respondeu com bom')
else:
    porcentagem = (qtd_bom / pessoas) * 100
    print(f'A porcentagem das pessoas que responderam bom foi {porcentagem:.2f}%')
