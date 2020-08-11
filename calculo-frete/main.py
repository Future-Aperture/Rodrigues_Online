from functions import showMenu, line, Produto, header, number, Options

header("PRECIFICAÇÃO")

options = Options()
produto = Produto(options)

while True:
    showMenu()
    line()
    opcao = number("Digite sua opção:\n> ")
    line()

    if opcao == 0:
        print("Programa finalizado. Pressione ENTER para sair.", end = "")
        input()
        break

    elif opcao == 1:
        vFrete = produto.calcFrete()
        line()

        if type(vFrete) == float:
            vFrete = f"{vFrete:.2f}"
            print(f"O valor do frete ficou: R$ {vFrete.replace('.', ',')}")

        else:
            vF0 = f"{vFrete[0]:.2f}"
            vF1 = f"{vFrete[1]:.2f}"
            print(f"""Caso o preço do produto seja abaixo de R$ 120.\nFrete: {vF0.replace('.', ',')}\n\nCaso o preço do produto seja acima de R$ 120.\nFrete: {vF1.replace('.', ',')}""")
       
        line()

    elif opcao == 2:
        vProduto, pLucro = produto.calcPreco()
        vProduto = f"{round(vProduto, 2):.2f}"
        pLucro = f"{round(pLucro, 2):.2f}"

        line()

        print(f"O valor recomendado para a venda do produto é: R$ {vProduto.replace('.', ',')}\nPorcentagem de lucro da venda: {pLucro}%")
        line()

    elif opcao == 9:
        options.show()

        print("[A] Ativar ou Desativar\n[M] Mudar os Valores")

        opcao2 = input("> ").upper()

        if opcao2 == "A":
            options.showAtivo()
            print("WIP")
        
        elif opcao2 == "M":
            options.change()

    else:
        print("Opção invalida.\n")