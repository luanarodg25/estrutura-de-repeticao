totalInvestido = 0
jurosPagos = 0
while True:
    codigo = int(input('Código do cliente (ou 0 para encerrar o programa): '))
    if codigo == 0:
        print('Programa encerrado')
        break
    tipo = int(input('Tipo de investimento: '))
    
    if tipo != 1 and tipo!= 2 and tipo !=3:
        print('Tipo inválido, digite 1,2 ou 3')
        continue

    valor = float(input('Informe o valor investido: '))

    if tipo == 1:
        rendimento = (1.5/100)* valor
    elif tipo == 2:
        rendimento = (2/100)* valor
    else:
        rendimento = (4/100)* valor

    totalInvestido += valor
    jurosPagos += rendimento
print(f'O total investido foi {totalInvestido:.2f}')
print(f'O total de juros pagos é {jurosPagos:.2f}')


    
    
