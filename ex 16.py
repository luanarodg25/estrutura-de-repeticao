somaIdade = 0
contIdade = 0

while True:
    idade = int(input('Informe a idade: '))

    if idade == 0:
        print('Programa encerrado')
        break

    somaIdade += idade
    contIdade += 1
    
if contIdade == 0:
    print('Nenhuma idade foi inserida')
else:
    media = somaIdade/contIdade
    print(f'A média das idades digitadas é {media:.2f}')
    
