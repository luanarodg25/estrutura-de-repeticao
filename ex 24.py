
valor = int(input('Informe um valor(ou 0 para encerrar): '))
if valor == 0:
    print('Nenhum valor foi inserido')
else:
    maiorV = valor
    menorV = valor
    
    while True:
        valor = int(input('Informe um valor(ou 0 para encerrar): '))

        if valor == 0:
            print('Programa encerrado')
            break
        
        
        if valor < 0:
            print('Valor negativo, não será contabilizado')
            continue
            
        if valor > 0:
            
            if valor > maiorV:
                maiorV = valor
            elif valor < menorV:
                menorV = valor
                
    print('O maior número é',maiorValor)
    print('O menor número é',menorValor)

                
            

    
