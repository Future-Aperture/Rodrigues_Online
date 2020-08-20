# <---------------| Modulos |--------------->
from decimal import Decimal, getcontext
import os


# <---------------| Variáveis Globais |--------------->
getcontext().prec = 10


# <---------------| Linha |--------------->
def linha():
    print()
    print("-=" * 30)
    print()


# <---------------| Header |--------------->
def header(msg):
    linha()
    print(f"{msg:^60}")
    linha()

# <---------------| Clean |--------------->
def clean(num):
    return f"{round(num, 2):.2f}".replace('.', ',')

# <---------------| Menu |--------------->
def showMenu():
    header("MENU PRINCIPAL")
    print("""[1] Calcular Frete
[2] Calcular Preço de Venda [Com Frete Grátis]
[3] Calcular Preço de Venda [Sem Frete Grátis]

[9] Opções
[0] Sair""")


# <---------------| Frete |--------------->
def fretePreco(p):
    if p < 0.5:
        return [47.90, 35.93]

    elif 0.5 <= p < 1:
        return [52.90, 39.68]

    elif 1 <= p < 2:
        return [61.90, 46.43]

    elif 2 <= p < 5:
        return [75.90, 56.93]

    elif 5 <= p < 9:
        return [97.90, 73.43]

    elif 9 <= p < 13:
        return [140.90, 105.68]

    elif 13 <= p < 17:
        return [187.90, 140.93]

    elif 17 <= p < 23:
        return [209.90, 157.43]

    elif 23 <= p < 29:
        return [219.90, 164.93]

    else:
        return [229.90, 172.43]


# <---------------| Número |--------------->
def number(msg = "> "):
    while True:
        num = input(msg)
        try:
            num = float(num.replace(",", "."))
            return num
        except:
            print(f"\n'{num}' não é um valor reconhecido. Tente novamente.\n")


class Options:
    embalagem = 3
    adicionalML = 5

    taxaML = 16.5 / 100
    imposto = 15 / 100
    lucro = 20 / 100

    multInicial = 1.01

    def show(self):
        header("OPÇÕES")
        print(f"""- Todos -
Multiplicador Inicial
Embalagem
Imposto
Lucro Mínimo

- Mercado Livre -
Adicional ML (Apenas e o produto custar menos de R$ 99,00)
Taxa ML\n""")

    def showAtivo(self):
        os.system('cls')
        header("OPÇÕES")

        print(f"""- Todos -
Multiplicador Inicial (X) [Não pode ser desativado]
Embalagem = (X)
Imposto = (X)
Lucro Mínimo = (X)

- Mercado Livre -
Adicional ML = (X)
Taxa ML = (X)""")
        print("\nWIP")
        linha()

        input("Pressione ENTER para continuar.")
        os.system('cls')

    def showChange(self):
        header("OPÇÕES")

        print(f"""- Todos -
[1] Multiplicador Inicial = {clean(self.multInicial)}x
[2] Embalagem = R$ {clean(self.embalagem)}
[3] Imposto = {clean(self.imposto * 100)}%
[4] Lucro Mínimo = {clean(self.lucro * 100)}%

- Mercado Livre -
[5] Adicional ML = R$ {clean(self.adicionalML)}
[6] Taxa ML = {clean(self.taxaML * 100)}%\n""")

    def change(self):
        while True:
            os.system('cls')

            self.showChange()
            print("Qual opção deseja alterar?\n'0' (zero) para voltar.\n")

            escolha = number("> ")

            if escolha == 0:
                os.system('cls')
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
                print("\nOpção Inválida.\n")
                continue

class Produto:
    frete = 0
    custo = 0

    def __init__(self, opcoes):
        self.opcoes = opcoes
            

    def calcFrete(self):
        print("""Para calcular o frete, precisamos do peso volumétrico do produto.\n\nInsira os valores pedidos:\n""")

        lar = number("Largura [cm]: ")
        alt = number("Altura [cm]: ")
        comp = number("Comprimento [cm]: ")

        pesoFis = number("\nPeso Físico [kg]: ")

        pesoVol = round(lar * alt * comp / 6000, 2)

        if pesoVol <= 5:
            peso = pesoFis

        else:
            peso = max([pesoVol, pesoFis])

        frete = fretePreco(peso)

        self.lar, self.alt, self.comp, self.pesoFis, self.pesoVol, self.frete = lar, alt, comp, pesoFis, pesoVol, frete

        return frete
        

    def calcPreco(self, freteGratis = True):
        multLocal = self.opcoes.multInicial

        if freteGratis:
            while True: 
                if bool(self.frete):
                    while True:
                        os.system("cls")
                        header("PREÇO COM FRETE")

                        print(f"""Caso o preço de venda seja abaixo de R$ 99,00.\nFrete: R$ {clean(self.frete[0])}\n\nCaso o preço de venda seja acima de R$ 99,00.\nFrete: R$ {clean(self.frete[1])}""")
                        linha()

                        resp = number(f"Dos valores de frete calculados, digite qual deles deseja usar.\n\n[1] R$ {clean(self.frete[0])}\n[2] R$ {clean(self.frete[1])}\n[3] Calcular um novo frete.\n\n> ")
                        print()

                        if resp == 1:
                            frete = self.frete[0]
                        
                        elif resp == 2:
                            frete = self.frete[1]

                        elif resp == 3:
                            os.system("cls")
                            header("PREÇO COM FRETE")
                            self.frete = self.calcFrete()
                            continue

                        else:
                            print("\nOpção inválida.\n")
                            continue

                        break

                else:
                    print("Para prosseguir é necessario calcular o frete do produto:")

                    frete = self.calcFrete()
                    self.frete = frete

                    linha()

                    continue

                break

        custo = number("Digite o valor de custo do produto.\n> R$ ")
        self.custo = custo

        while True:
            vLucro = 0
            valorFinal = self.custo + self.opcoes.embalagem

            if freteGratis:
                valorFinal += frete
                vLucro -= frete

            valorFinal *= multLocal
                
            if valorFinal <= 99:
                valorFinal += self.opcoes.adicionalML
                vLucro -= self.opcoes.adicionalML

            vImposto = round(valorFinal * self.opcoes.imposto, 2)
            vTaxaML = round(valorFinal * self.opcoes.taxaML, 2)

            vLucro += valorFinal - vImposto - vTaxaML - self.opcoes.embalagem - self.custo
            vLucro = round(vLucro, 2)

            multLocal = float(f"{Decimal(multLocal) + Decimal(0.01):.2f}")

            if vLucro >= self.custo * self.opcoes.lucro:   
                porLucro = round(vLucro / self.custo, 4) * 100      

                lNomes = ["Custo", "Lucro", "Imposto", "Taxa ML", "Embalagem"]
                lValores = [self.custo, vLucro, vImposto, vTaxaML, self.opcoes.embalagem]

                if valorFinal <= 99:
                    lNomes.append("Adicional ML")
                    lValores.append(self.opcoes.adicionalML)
                
                if freteGratis:
                    lNomes.insert(2, "Frete")
                    lValores.insert(2, frete)
                
                return valorFinal, porLucro, dict(zip(lNomes, lValores))