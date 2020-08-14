
class Obj:
    lucro = 20/100
    imposto = 15/100
    embalagem = 3



def titulo(msg):
    print('-='*30)
    print(f'{msg:^60}')
    print('-='*60)

def lin():
    print('-'*30)


def menu():
    print('''
[ 1 ] Calcular um produto (produto+frete+lucro+embalagem)
[ 2 ] Calcular produto + frete
[ 0 ] Sair
    ''')


def baixoPreço(p):
    if p < 0.5:
        return 47.90

    elif 0.5 <= p < 1:
        return 52.90

    elif 1 <= p < 2:
        return 61.90

    elif 2 <= p < 5:
        return 75.90

    elif 5 <= p < 9:
        return 97.90

    elif 9 <= p < 13:
        return 140.90 

    elif 13 <= p < 17:
        return 187.90

    elif 17 <= p < 23:
        return 209.90

    elif 23 <= p < 29:
        return 219.90

    else:
        return 229.90


def altoPreco(p):
    if p < 0.5:
        return 35.93

    elif 0.5 <= p < 1:
        return 39.68

    elif 1 <= p < 2:
        return 46.43

    elif 2 <= p < 5:
        return 56.93

    elif 5 <= p < 9:
        return 73.43

    elif 9 <= p < 13:
        return 105.68 

    elif 13 <= p < 17:
        return 140.93

    elif 17 <= p < 23:
        return 157.43

    elif 23 <= p < 29:
        return 164.93

    else:
        return 172.43
