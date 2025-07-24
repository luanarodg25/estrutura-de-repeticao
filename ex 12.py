qtd_primos = 0
for i in range(10):
    numero = int(input(f'Informe o {i+1} número: '))

    if numero < 2:
        continue

    divisores = 0
    for j in range (1,numero+1):
        if numero % j == 0:
            divisores += 1

    if divisores == 2:
        qtd_primos += 1
            
print('A quantidade de números primos entre os números digitados é',qtd_primos)
    
