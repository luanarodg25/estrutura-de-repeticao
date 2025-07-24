valor = float(input("Informe o valor do carro: R$ "))

preco_final = valor * 0.80
print(f'\nPreço final com desconto de 20%: R$ {preco_final:.2f}\n')

parcelas = 6
aumento = 3

print(f'{"Parcelas":<10}{"Valor da parcela":<20}{"Preço Final":<15}')

while parcelas <= 60:
    valor_total = valor + (valor * aumento / 100)
    valor_parcela = valor_total / parcelas

    print(f'{parcelas:<10}{f"R$ {valor_parcela:.2f}":<20}{f"R$ {valor_total:.2f}":<15}')

    parcelas += 6
    aumento += 3
