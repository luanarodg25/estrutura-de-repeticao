somaIdade = 0
qtdPA = 0
qtdAlturaSuperior = 0
qtd_pessoas = 10
qtdIdade1030 = 0

for i in range(qtd_pessoas):
    idade = int(input(f'Informe a idade da {i+1}ª pessoa: '))
    peso = int(input(f'Informe o peso da {i+1}ª pessoa: '))
    altura = float(input(f'Informe a altura da {i+1}ª pessoa: '))

    somaIdade += idade

    if peso > 90 and altura < 1.50:
        qtdPA += 1

    if altura > 1.90:
        qtdAlturaSuperior += 1
        if 10 <= idade <= 30:
            qtdIdade1030 += 1

if qtd_pessoas == 0:
    print('Nenhuma pessoa foi inserida')
else:
    media = somaIdade / qtd_pessoas
    print(f'A média das idades das {qtd_pessoas} pessoas é {media:.2f}')

    if qtdAlturaSuperior == 0:
        print('Nenhuma pessoa com altura superior a 1.90 foi inserida. Não é possível calcular a porcentagem.')
    else:
        porcentagem = (qtdIdade1030 / qtdAlturaSuperior) * 100
        print(f'A porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1.90 é {porcentagem:.2f}%')
