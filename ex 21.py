total1= 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
qtd5 = 0
qtd6 = 0
TOTAL = 0
print('1,2,3,4 Votos para os respectivos candidatos')
print('5 voto nulo')
print('6 voto branco')
while True:
    voto = int(input('Informe seu voto ou 0 para encerrar: '))
    if voto > 6 or voto < 0:
        print('Voto inválido')
        continue
    if voto == 0:
        print('Votação encerrada')
        break
    
    if voto == 1:
        total1 += 1
    elif voto == 2:
        total2 += 1
    elif voto == 3:
        total3 += 1
    elif voto == 4:
        total4 += 1

    if voto == 5:
        qtd5 += 1
    if voto == 6:
        qtd6 += 1

    TOTAL += voto
print('Candidato 1:',total1)
print('Candidato 2:',total2)
print('Candidato 3:',total3)
print('Candidato 4:',total4)
print('Votos nulos:',qtd5)
print('Votos em branco:',qtd6)

if qtd5 == 0:
    print('Não houve voto nulo')
else:
    porcentagem5 = (qtd5/TOTAL)*100
    print(f'porcentagem de voto nulo sobre o total de votos {porcentagem5:.2f}%')
    
if qtd6 == 0:
    print('Não houve voto em branco')
else:
    porcentagem6 = (qtd6/TOTAL)*100
    print(f'porcentagem de voto nulo sobre o total de votos {porcentagem6:.2f}%')


    
