pessoas = 0
rsim = 0
rnao = 0
homemNao = 0
mulherSim = 0
respostahomemNao = 0
while pessoas < 10:
    while True:
        sexo = input('Informe o sexo: ').upper()
        resposta = input('Informe se gostou ou não do produto (S - sim | N - não): ').upper()

        if resposta in ['S', 'N'] and sexo in ['F', 'M']:
            break
        else:
            print('Resposta inválida, digite F ou M para sexo e S ou N para resposta!')

    if resposta == 'S':
        rsim += 1
    else:
        rnao += 1
        
    if sexo == 'F' and resposta == 'S':
        mulherSim += 1

    if sexo == 'M':
        homemNao += 1
        if resposta == 'N':
            respostahomemNao += 1
            
    pessoas += 1

print(f'O número de pessoas que responderam sim {rsim}')
print(f'O número de pessoas que responderam não {rnao}')
print(f'O número de mulheres que responderam sim {mulherSim}')

if homemNao == 0:
    print('Nenhum homem respondeu "Não"')
else:
    porcentagem = (respostahomemNao/homemNao)*100
    print(f'A porcentagem de homens que responderam não entre todos os homens analisados é {porcentagem:.2f}%')
    
