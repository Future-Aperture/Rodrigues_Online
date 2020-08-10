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

    taxaML = 16 / 100
    imposto = 15 / 100
    lucro = 20 / 100


class Produto:

    frete = 0
    preco = 0

    def calcFrete(self, twoValues = True):
        print("""Para calcularmos o valor do frete, primeiros precisamos do peso volumétrico do produto.
Insira os valores pedidos a baixo.\n""")

        lar = number("Largura [cm]: ")
        alt = number("Altura [cm]: ")
        comp = number("Comprimento [cm]: ")

        pesoFis = number("\nPeso Físico [kg]: ")

        print("\nHá dois possiveis valores de frete dependendo do preço do produto.\n")

        if twoValues:
            print("Caso queira os dois, insira '0' (zero) como valor do preço.\n")

        preco = number("Preço: R$ ")

        pesoVol = round(lar * alt * comp / 6000, 2)

        if pesoVol <= 5:
            peso = pesoFis

        else:
            peso = max([pesoVol, pesoFis])

        frete = [baixoPreço(peso), altoPreco(peso)]

        self.lar, self.alt, self.comp, self.pesoFis, self.preco, self.pesoVol, self.frete = lar, alt, comp, pesoFis, preco, pesoVol, frete

        while True:
            if preco < 120 and preco != 0:
                return frete[0]

            elif preco >= 120:
                return frete[1]

            else:
                if twoValues:
                    return frete
                else:
                    print("\nNão podemos calcular o preco com dois valores de frete, por favor, insira um preço.")
                    preco = number("\nPreço: R$ ")
                    self.preco = preco
                    continue

    def calcPreco(self):
        if bool(self.frete) and bool(self.preco):
            while True:
                resp = input("Deseja usar o valor do ultimo frete calculado? [S/N]\n> ").upper()

                if resp == "N":
                    frete = self.calcFrete(twoValues = False)
                
                elif resp == "S":
                    if len(self.frete) == 2:
                        if self.preco < 120:
                            frete = self.frete[0]
                        else:
                            frete = self.frete[1]
                    else:
                        frete = self.frete
                else:
                    print("Opção invalida.")
                    continue

                break
        else:
            frete = self.calcFrete(twoValues = False)
            self.frete = frete

        vImposto = (self.preco + self.frete) * Options.imposto
        vTaxaML = self.preco * Options.taxaML

        precoFinal = self.frete + self.preco + Options.embalagem + vImposto + vTaxaML

        if self.preco < 120:
            precoFinal += 5

        return precoFinal