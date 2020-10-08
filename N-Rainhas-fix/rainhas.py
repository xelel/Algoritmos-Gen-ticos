from abc import abstractmethod
from random import randint, sample, choices, shuffle, choice, randrange
from individuo import Individuo
from itertools import count


class Rainhas(Individuo):

    def __init__(self, n):
        self.n = n
        self.lista_Rainhas = [0]*n
        self.aval = None

    def definir_posicoes_rainha(self):
        self.lista_Rainhas = sample(range(1, self.n+1), self.n)

    def __len__(self):
        return len(self.lista_Rainhas)

    def __setitem__(self, k, val):
        self.lista_Rainhas[j] = val

    def __getitem__(self, j):
        return self.lista_Rainhas[j]

    def __str__(self):
        # Representação formada do vector
        return str(self.lista_Rainhas)

        # recombinar

    def __add__(self, element):

        if len(self) != len(element):
            raise ValueError('os vetores de rainhas devem ter tamanhos iguais')

        corte = randrange(0, len(self)-1)
        filho = Rainhas(self.n)

        # cria um filho, com base na posicao do corte gerado
        filho.lista_Rainhas = self[0:corte] + element[corte:self.n]
        indice_repetido = []

        # procura indice de rainhas repetidas e adiciona em uma lista
        for i in filho.lista_Rainhas[0:corte]:
            try:

                if filho.lista_Rainhas.count(i) > 1:
                    indice_repetido.append(filho.lista_Rainhas.index(
                        i, corte, self.n))

            except ValueError:
                return
        # Numeros que estão faltando no vetor de rainhas
        num_faltantes = [n for n in range(
            1, len(self)+1) if n not in filho.lista_Rainhas]

        # mistura os numeros faltantes
        num_faltantes = sample(num_faltantes, len(num_faltantes))
        for pos, indice in enumerate(indice_repetido):
            filho.lista_Rainhas[indice] = num_faltantes[pos]

        return filho

    def avaliacao(self):
        try:
            self.aval = (1/self.colisao())
            return self.aval
        except(ZeroDivisionError):
            return
    # colisao entre rainhas

    def colisao(self):
        contador = 0
        for i in range(len(self)):
            for j in range(1+i, len(self)):
                if self.lista_Rainhas[i] == self.lista_Rainhas[j]+abs(i-j):
                    contador += 1
                elif self.lista_Rainhas[i] == self.lista_Rainhas[j]-abs(i-j):
                    contador += 1
        return contador

    def mutar(self):
        rainhas_aleatorias = sample(self.lista_Rainhas, 2)
        r_1, r_2 = rainhas_aleatorias
        pos_r_1 = self.lista_Rainhas.index(r_1)
        pos_r_2 = self.lista_Rainhas.index(r_2)

        self.lista_Rainhas[pos_r_1], self.lista_Rainhas[pos_r_2] = r_2, r_1
        return self


if __name__ == "__main__":
    r = Rainhas(10)
    r1 = Rainhas(10)
    r.definir_posicoes_rainha()
    r1.definir_posicoes_rainha()
    print(r)
    r.avaliacao()
    print(r+r1)
    print(r1+r)
