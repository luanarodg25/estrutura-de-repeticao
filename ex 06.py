totalV = 0
totalP = 0
totalCompras = 0
prestacao = 0
for i in range(3):
    codigo = input('Informe o código da transação (V - à vista ou P - a prazo: ').upper()
    valor = float(input(f'Informe o valor da {i+1} transação: ' ))

    if codigo == 'V':
        totalV += valor
    elif codigo == 'P':
        totalP += valor
        prestacao = totalP / 3
    else:
        print('Código inválido, insira V ou P')

    totalCompras += valor
    
print(f'Valor total à vista: {totalV:.2f}')
print(f'Valor total a prazo: {totalP:.2f}')
print(f'Valor total das compras feitas: {totalCompras:.2f}')
print(f'Primeira prestação das compras a prazo: {prestacao:.2f}')
