from functions import showMenu, line, Produto, header, number

header("PRECIFICAÇÃO")

showMenu()
line()

produto = Produto()

while True:
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
            print(f"O valor do frete ficou: R$ {str(vFrete).replace('.', ',')}")
        else:
            vF0 = f"{vFrete[0]:.2f}"
            vF1 = f"{vFrete[1]:.2f}"
            print(f"""Caso o preço do produto seja abaixo de R$ 120.
Frete: {vF0.replace('.', ',')}

Caso o preço do produto seja acima de R$ 120.
Frete: {vF1.replace('.', ',')}""")
       
        line()

        showMenu()
        line()
    
    elif opcao == 2:
        vProduto = produto.calcPreco()
        print(vProduto)

    else:
        print("Opção invalida.\n")


