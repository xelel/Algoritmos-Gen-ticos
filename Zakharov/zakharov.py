from abc import abstractmethod
from random import randint, sample, choices, shuffle, choice, randrange, uniform, gauss
from individuo import Individuo
from itertools import count


class Zakharov(Individuo):

    def __init__(self, d):
        self.d = d
        self.zakharov_entrada = [0]*d
        self.melhor_entrada = None

    def definir_entradas_aleatorias(self):
        self.zakharov_entrada = [uniform(-5, 10) for i in range(self.d)]

    def __len__(self):
        return len(self.zakharov_entrada)

    def __getitem__(self, j):
        return self.zakharov_entrada[j]

    def __str__(self):
        # Representação formada do vector
        return str(self.zakharov_entrada)

        # recombinar
    def __add__(self, element):
        alpha = 0.33
        filho = Zakharov(len(self))
        filho.zakharov_entrada = [
            (1-alpha)*self[i]+(alpha*element[i]) for i in range(self.d)]
        return filho

    def funcao(self):
        for v in self.zakharov_entrada:
            saida_Func = 0
            somatorio1 = 0
            somatorio2 = 0
            somatorio3 = 0

            for d in range(self.d):
                somatorio1 += v**2
                somatorio2 += ((0.5)*d*v)**2
                somatorio3 += ((0.5)*d*v)**4
                saida_Func += somatorio1 + somatorio2 + somatorio3
            yield saida_Func

    def avaliacao(self):
        melhor_av = None
        for valor in self.funcao():

            if melhor_av == None:
                melhor_av = valor
            if valor < melhor_av:
                melhor_av = valor
                self.melhor_entrada = valor

        return melhor_av

    def mutar(self):
        cont = 0
        for i in self.zakharov_entrada:
            gausiana = gauss(0, 1)

            if 0 < gausiana <= 0.1:
                cont = 1
                i = i + gausiana

                if i > 10:
                    i = randrange(-5, 10)

                return self

        if cont == 0:
            pos_aleatoria = randrange(0, self.d-1)

            self.zakharov_entrada[pos_aleatoria] = uniform(-5, 10)

            return self


if __name__ == "__main__":
    r = Zakharov(5)
    r.definir_entradas_aleatorias()
    r1 = Zakharov(5)
    r1.definir_entradas_aleatorias()
    print(r)

    print('=-'*15)

    print(r+r1)
