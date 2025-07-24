somaSalario = 0
qtd_mulher = 0
qtd_pessoas = 0

# Primeiro cadastro fora do loop
idade = int(input('Informe a idade (ou digite um número negativo para encerrar o programa): '))

if idade < 0:
    print('Nenhuma pessoa foi inserida.')
else:
    sexo = input('Informe o sexo (M/F): ').upper()
    salario = float(input('Informe o salário: '))

    maiorIdade = idade
    menorIdade = idade
    menorSalario = salario

    if sexo == 'F' and salario < 200:
        qtd_mulher += 1

    qtd_pessoas += 1
    somaSalario += salario

    while True:
        idade = int(input('Informe a idade (ou digite um número negativo para encerrar o programa): '))
        if idade < 0:
            print('Programa encerrado')
            break

        sexo = input('Informe o sexo (M/F): ').upper()
        salario = float(input('Informe o salário: '))

        if idade > maiorIdade:
            maiorIdade = idade
        if idade < menorIdade:
            menorIdade = idade
        if salario < menorSalario:
            menorSalario = salario

        if sexo == 'F' and salario < 200:
            qtd_mulher += 1

        qtd_pessoas += 1
        somaSalario += salario

    media = somaSalario / qtd_pessoas
    print(f'\nA média dos salários do grupo é R$ {media:.2f}')
    print(f'A maior idade do grupo é {maiorIdade}')
    print(f'A menor idade do grupo é {menorIdade}')
    print(f'A quantidade de mulheres com salário até R$ 200,00 é {qtd_mulher}')
