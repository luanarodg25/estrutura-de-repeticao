somaPares = 0
somaPrimos = 0

for i in range(10):
    numero = int(input(f'Digite o {i+1}º número: '))

    if numero % 2 == 0:
        somaPares += numero

    if numero > 1:
        divisores = 0
        for j in range(1, numero + 1):
            if numero % j == 0:
                divisores += 1
                if divisores == 2:
                    somaPrimos += numero

print('Soma dos números pares:', somaPares)
print('Soma dos números primos:', somaPrimos)
