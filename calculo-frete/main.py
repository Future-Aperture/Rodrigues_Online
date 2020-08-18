from functions import showMenu, line, Produto, header, number, Options
import os

os.system('cls')

header("AFTON")

options = Options()
produto = Produto(options)

while True:
    showMenu()
    line()
    opcao = number("Sua opção:\n> ")
    line()

    if opcao == 0:
        os.system('cls')
        header("AFTON")
        print("Programa finalizado. Pressione ENTER para sair.", end = "")
        input()
        break

    elif opcao == 1:
        os.system('cls')
        header("FRETE")
        vFrete = produto.calcFrete()
        line()

        if type(vFrete) == float:
            vFrete = f"{vFrete:.2f}"
            print(f"O valor do frete ficou: R$ {vFrete.replace('.', ',')}")

        else:
            vF0 = f"{vFrete[0]:.2f}"
            vF1 = f"{vFrete[1]:.2f}"
            print(f"""Caso o preço de venda seja abaixo de R$ 99,00.\nFrete: R$ {vF0.replace('.', ',')}\n\nCaso o preço de venda seja acima de R$ 99,00.\nFrete: R$ {vF1.replace('.', ',')}""")
       
        line()
        input("Pressione ENTER para continuar.")
        os.system('cls')

    elif opcao == 2:
        os.system('cls')
        header("PREÇO COM FRETE")
        vProduto, pLucro, dictValores = produto.calcPreco()
        vProduto = f"{round(vProduto, 2):.2f}"
        pLucro = f"{round(pLucro, 2):.2f}"

        os.system('cls')
        header("PREÇO COM FRETE")

        print(f"O valor recomendado para a venda do produto é: R$ {vProduto.replace('.', ',')}\nPorcentagem de lucro da venda: {pLucro.replace('.',',')}%")
        line()

        for k, v in dictValores.items():
            v = f"{v:.2f}"
            print(f"{k} = R$ {v.replace('.', ',')}")

        line()
        input("Pressione ENTER para continuar.")
        os.system('cls')

    elif opcao == 3:
        os.system('cls')
        header("PREÇO SEM FRETE")
        vProduto, pLucro, dictValores = produto.calcPreco(freteGratis = False)
        vProduto = f"{round(vProduto, 2):.2f}"
        pLucro = f"{round(pLucro, 2):.2f}"

        line()

        os.system('cls')
        header("PREÇO COM FRETE")
        print(f"O valor recomendado para a venda do produto é: R$ {vProduto.replace('.', ',')}\nPorcentagem de lucro da venda: {pLucro}%")
        line()

        for k, v in dictValores.items():
            v = f"{v:.2f}"
            print(f"{k} = R$ {v.replace('.', ',')}")

        line()
        input("Pressione ENTER para continuar.")
        os.system('cls')

    elif opcao == 9:
        os.system('cls')
        options.show()

        print("[A] Ativar/Desativar\n[M] Mudar os Valores")

        opcao2 = input("> ").upper()

        if opcao2 == "A":
            options.showAtivo()
            line()
        
        elif opcao2 == "M":
            options.change()

    else:
        print("Opção inválida.\n")