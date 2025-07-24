preco_ingresso = 5
qtd_ingresso = 120
despesas = 200
lucroMaximo = 0 
precoM = 0
qtdM = 0
print(f'{"Preço":>10} {"Quantidade":>15} {"Lucro":>10}')
while preco_ingresso >= 1:
    lucroEsperado = (preco_ingresso * qtd_ingresso) - despesas

    if lucroEsperado > lucroMaximo:
        lucroMaximo = lucroEsperado
        precoM = preco_ingresso
        qtdM = qtd_ingresso


    print(f'{preco_ingresso:>10} {qtd_ingresso:>15} {lucroEsperado:>10}')

    qtd_ingresso += 26
    preco_ingresso -= 0.5

print(f'O lucro máximo foi:{lucroMaximo}')
print(f'Quantidade de ingresso nesse lucro máximo:{qtdM}')
print(f'preço do ingresso nesse lucro máximo:{precoM}')
