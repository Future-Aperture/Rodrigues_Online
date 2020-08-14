from decimal import Decimal, getcontext

getcontext().prec = 10

def line():
    print()
    print("-=" * 30)
    print()


def header(msg):
    line()
    print(f"{msg:^60}")
    line()


def showMenu():
    print("""[1] Calcular Frete
[2] Calcular Preço de Venda
[9] Opções
[0] Sair""")


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


def number(msg):
    while True:
        num = input(msg)
        try:
            num = float(num.replace(",", "."))
            return num
        except:
            print(f"\n'{num}' não é um valor válido, tente novamente.\n")


class Options:
    embalagem = 3
    adicionalML = 5

    taxaML = 16.5 / 100
    imposto = 15 / 100
    lucro = 20 / 100

    multInicial = 1.1

    def show(self):
        print(f"""- Todos -
Multiplicador Inicial
Embalagem
Imposto
Lucro Mínimo

- Mercado Livre -
Adicional ML [Apenas caso o produto custe menos do que R$ 99,00]
Taxa ML\n""")

    def showAtivo(self):
        print(f"""- Todos -
Multiplicador Inicial [X] [Não pode ser desativado]
Embalagem = [X]
Imposto = [X]
Lucro Mínimo = [X]

- Mercado Livre -
Adicional ML = [X]
Taxa ML = [X]\n""")

    def showChange(self):
        emb = f"{self.embalagem:.2f}"
        aML = f"{self.adicionalML:.2f}"

        print(f"""- Todos -
[1]Multiplicador Inicial = {str(self.multInicial).replace(".", ",")}x
[2]Embalagem = R$ {emb.replace(".", ",")}
[3]Imposto = {str(self.imposto * 100).replace(".", ",")}%
[4]Lucro Mínimo = {str(self.lucro * 100).replace(".", ",")}%

- Mercado Livre -
[5]Adicional ML = R$ {aML.replace(".", ",")}
[6]Taxa ML = {str(self.taxaML * 100).replace(".", ",")}%\n""")


    def change(self):
        while True:
            line()
            self.showChange()
            escolha = number("Qual opção deseja alterar?\n'0' (zero) para voltar.\n> ")

            if escolha == 0:
                line()
                break

            elif escolha == 1:
                self.multInicial = number("\nValor inicial do multiplicador\n> ")

            elif escolha == 2:
                self.embalagem = number("\nCusto da embalagem\n> R$ ")
            
            elif escolha == 3:
                self.imposto = number("\nPorcentagem de imposto\n> ") / 100

            elif escolha == 4:
                self.lucro = number("\nPorcentagem de lucro\n> ") / 100

            elif escolha == 5:
                self.adicionalML = number("\nCusto adicional do ML\n> ")

            elif escolha == 6:
                self.taxaML = number("\nPorcentagem da taxa adicional do ML\n> ") / 100

            else:
                print("\nOpção Invalida.")
                continue


class Produto:

    def __init__(self, op):
        self.opcao = op

    frete = 0
    custo = 0

    def calcFrete(self):
        print("""Para calcularmos o valor do frete, primeiro precisamos do peso volumétrico do produto.\n\nInsira os valores pedidos a baixo.\n""")

        lar = number("Largura [cm]: ")
        alt = number("Altura [cm]: ")
        comp = number("Comprimento [cm]: ")

        pesoFis = number("\nPeso Físico [kg]: ")

        pesoVol = round(lar * alt * comp / 6000, 2)

        if pesoVol <= 5:
            peso = pesoFis

        else:
            peso = max([pesoVol, pesoFis])

        frete = [baixoPreço(peso), altoPreco(peso)]

        self.lar, self.alt, self.comp, self.pesoFis, self.pesoVol, self.frete = lar, alt, comp, pesoFis, pesoVol, frete

        return frete
        

    def calcPreco(self):
        vLucro, porLucro = 0, 0
        multLocal = self.opcao.multInicial

        while True:
            if bool(self.frete):
                while True:
                    vF0 = f"{self.frete[0]:.2f}"
                    vF1 = f"{self.frete[1]:.2f}"
                    resp = number(f"Dos valores de frete calculados, digite qual deles deseja usar.\n[1]R$ {vF0.replace('.', ',')}\n[2]R$ {vF1.replace('.', ',')}\n[3]Calcular um novo frete.\n\n> ")

                    if resp == 1:
                        frete = self.frete[0]
                    
                    elif resp == 2:
                        frete = self.frete[1]

                    elif resp == 3:
                        frete = self.calcFrete()
                        self.frete = frete

                    else:
                        print("\nOpção invalida.\n")
                        continue

                    break

            else:
                print("Para conseguir-mos prosseguir, primeiro é necessario calcular-mos o frete do produto.")

                frete = self.calcFrete()
                self.frete = frete

                line()

                continue

            break

        custo = number("\nDigite o valor de custo do produto.\n> R$ ")
        self.custo = custo

        while True:
            valorFinal = frete + self.custo + self.opcao.embalagem
                
            valorFinal *= multLocal

            vImposto = valorFinal * self.opcao.imposto
            vTaxaML = valorFinal * self.opcao.taxaML

            if valorFinal <= 99:
                valorFinal += self.opcao.adicionalML

            vLucro = valorFinal - vImposto - vTaxaML - self.opcao.embalagem - frete - self.custo

            if valorFinal <= 99:
                vLucro -= self.opcao.adicionalML

            multLocal = float(f"{Decimal(multLocal) + Decimal(0.1):.2f}")
        
            porLucro = round(vLucro / self.custo, 4) * 100

            if vLucro >= self.custo * self.opcao.lucro:
                break

        return valorFinal, porLucro