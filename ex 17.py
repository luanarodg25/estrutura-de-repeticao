qtdcanal4 = 0
qtdcanal5 = 0
qtdcanal7 = 0
qtdcanal12 = 0
total_pessoas = 0
while True:
    canal = int(input('Informe o canal utilizado (4,5,7 ou 12), se quiser encerrar o programa digite 0: '))
    if canal == 0:
        print('Programa encerrado')
        break
    
    pessoas = int(input('Informe a quantidade de pessoas assistindo esse canal: '))

    if canal == 4:
        qtdcanal4 += pessoas
        
    elif canal == 5:
        qtdcanal5 += pessoas
        
    elif canal == 7:
        qtdcanal7 += pessoas
        
    elif canal == 12:
        qtdcanal12 += pessoas

    total_pessoas += pessoas

if qtdcanal4 == 0:
    print(f'Nenhuma pessoa foi inserida no canal 4')
else:
    porcentagem4 = (qtdcanal4/total_pessoas)*100
    print(f'A porcentagem de audiência do canal 4 é {porcentagem4:.2f}%')
    
if qtdcanal5 == 0:
    print(f'Nenhuma pessoa foi inserida no canal 5')
else:
    porcentagem5 = (qtdcanal5/total_pessoas)*100
    print(f'A porcentagem de audiência do canal 5 é {porcentagem5:.2f}%')
    
if qtdcanal7 == 0:
    print(f'Nenhuma pessoa foi inserida no canal 7')
else:
    porcentagem7 = (qtdcanal7/total_pessoas)*100
    print(f'A porcentagem de audiência do canal 7 é {porcentagem7:.2f}%')
    
if qtdcanal12 == 0:
    print(f'Nenhuma pessoa foi inserida no canal 12')
else:
    porcentagem12 = (qtdcanal12/total_pessoas)*100
    print(f'A porcentagem de audiência do canal 12 é {porcentagem12:.2f}%')
      
        

    
