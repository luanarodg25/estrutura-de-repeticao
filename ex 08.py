qtd_50Peso = 0
somaIdade = 0
qtdIdade = 0
qtdOlhosazuis = 0
qtdR_A = 0
quantidade_pessoas = 6

for i in range(quantidade_pessoas):
    idade = int(input(f'Informe a idade da {i+1}ª pessoa: '))
    peso = int(input(f'Informe o peso da {i+1}ª pessoa: '))
    altura = float(input(f'Informe a altura da {i+1}ª pessoa: '))

    while True:
        cor_olhos = input(f'Informe a cor dos olhos da {i+1}ª pessoa (A — azul; P — preto; V — verde; C — castanho): ').upper()
        if cor_olhos in ['A', 'P', 'V', 'C']:
            break
        print('Cor de olhos inválida! Digite apenas A, P, V ou C.')

    while True:
        cor_cabelos = input('Cor do cabelo (P — preto; C — castanho; L — louro; R — ruivo): ').upper()
        if cor_cabelos in ['P', 'C', 'L', 'R']:
            break
        print('Cor inválida! Digite apenas P, C, L ou R.')

    if idade > 50 and peso < 60:
        qtd_50Peso += 1

    if altura < 1.50:
        qtdIdade += 1
        somaIdade += idade

    if cor_olhos == 'A':
        qtdOlhosazuis += 1

    if cor_cabelos == 'R' and cor_olhos != 'A':
        qtdR_A += 1

print(f'\nA quantidade de pessoas com mais de 50 anos e peso menor que 60kg: {qtd_50Peso}')

if qtdIdade == 0:
    print('Nenhuma pessoa com altura menor que 1.50 foi inserida')
else:
    media_idade = somaIdade / qtdIdade
    print(f'A média das idades das pessoas com altura inferior a 1.50m: {media_idade:.2f}')

if qtdOlhosazuis == 0:
    print('Nenhuma pessoa com olho azul foi inserida')
else:
    porcentagem = (qtdR_A / quantidade_pessoas) * 100
    print(f'A porcentagem de pessoas ruivas que não possuem olhos azuis: {porcentagem:.2f}%')
