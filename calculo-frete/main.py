# <---------------| Modulos |--------------->
from functions import showMenu, linha, Produto, header, number, Options, clean
import os

# <---------------| Variáveis Globais |--------------->
options = Options()
produto = Produto()
opcao = 0


while True:
    if opcao in [0, 1, 2, 3, 9]:
        os.system('cls')
        header("AFTON")
        showMenu()
        linha()

    opcao = number("Sua opção:\n> ")

    if opcao == 0:
        os.system('cls')
        header("AFTON")
        input("Programa finalizado. Pressione ENTER para sair.")
        break

    elif opcao == 1:
        os.system('cls')
        header("FRETE")
        vFrete = produto.calcFrete()
        linha()

        print(f"Caso o preço de venda seja abaixo de R$ 99,00.\nFrete: R$ {clean(vFrete[0])}\n\nCaso o preço de venda seja acima de R$ 99,00.\nFrete: R$ {clean(vFrete[1])}")
       
        linha()
        input("Pressione ENTER para continuar.")

    elif opcao == 2:
        os.system('cls')
        header("PREÇO COM FRETE")
        vProduto, pLucro, dictValores = produto.calcPreco()
        os.system('cls')
        
        header("PREÇO COM FRETE")

        print(f"O valor recomendado para a venda do produto é: R$ {clean(vProduto)}\nPorcentagem de lucro da venda: {clean(pLucro)}%")
        linha()

        for k, v in dictValores.items():
            print(f"{k} = R$ {clean(v)}")

        linha()
        input("Pressione ENTER para continuar.")

    elif opcao == 3:
        os.system('cls')
        header("PREÇO SEM FRETE")
        vProduto, pLucro, dictValores = produto.calcPreco(freteGratis = False)
        os.system('cls')
 
        header("PREÇO COM FRETE")

        print(f"O valor mínimo recomendado para a venda do produto é: R$ {clean(vProduto)}\nPorcentagem de lucro da venda: {clean(pLucro)}%")
        linha()

        for k, v in dictValores.items():
            print(f"{k} = R$ {clean(v)}")

        linha()
        input("Pressione ENTER para continuar.")

    elif opcao == 9:
        os.system('cls')

        while True:
            options.show()
            print("[A] Ativar/Desativar\n[M] Mudar os Valores\n[0] Voltar")

            while True:
                opcao2 = input("> ").upper()

                if opcao2 == "A":
                    options.showAtivo()
                    break
                
                elif opcao2 == "M":
                    options.change()
                    break

                elif opcao2 == "0":
                    break

                else:
                    print("\nOpção inválida.\n")
                
            if opcao2 == "0":
                    break

    else:
        print("\nOpção inválida.\n")
        opcao = None
        continue