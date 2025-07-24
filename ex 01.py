for i in range(1,6):
    print('Grupo',i)
    a = int(input('a) Digite um valor: '))
    b = int(input('b) Digite um valor: '))
    c = int(input('c) Digite um valor: '))
    d = int(input('d) Digite um valor: '))

    print(f'Ordem lida: {a},{b},{c},{d}')
    print()

    if a > b:
        a,b = b,a 
    if a > c:
        a,c = c,a 
    if a > d:
        a,d = d,a
    if b > c:
        b,c = c,b
    if b > d:
        b,d = d,b
    if c > d:
        c,d = d,c
    

    print(f'Ordem crescente: {a} {b} {c} {d}')
    print(f'Ordem decrescente: {d} {c} {b} {a}')


