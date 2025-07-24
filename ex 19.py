qtdSuperior = 0
qtdInferior = 0
somaLucro = 0
while True:
    acao = input('Informe o tipo de ação (para finalizar digite F): ').upper()
    if acao == 'F':
        print('Programa finalizado')
        break
    
    compra = float(input('Digite o valor de compra dessa ação: '))
    venda = float(input('Digite o valor de venda dessa ação: '))
    lucro = venda - compra

    print(f'O lucro dessa ação foi {lucro:.2f}')
    print('-'*70)

    if lucro > 1000:
        qtdSuperior += 1
    if lucro < 200:
        qtdInferior += 1
        
    somaLucro += lucro

print('A quantidade de ações com lucro maior de R$ 1.000,00',qtdSuperior)
print('A quantidade de ações com lucro menor que R$ 200,00',qtdInferior)
print(f'O lucro total da empresa é {somaLucro:.2f}')

    



