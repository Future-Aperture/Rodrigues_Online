from functions import menu, titulo, lin

titulo('CÁLCULO')


menu()
while True:
    try:
        op = int(input('Sua opção:\n> '))

    except:
        print('Digite um valor inválido.')
        
    if op == 1:
        print()
        titulo('opção 1!')
        p = float(input('Preço do item R$: '))
        peso = float(input('Peso do produto[kg]: '))
        alt = int(input('Insira a altura do item[cm]: '))
        larg = int(input('Insira a largura do item[cm]: '))
        comp = int(input('Insira o comprimento do item[cm]: '))
        print()


    if op == 0:
        titulo('Escolheu sair, até!')
        print()
        break