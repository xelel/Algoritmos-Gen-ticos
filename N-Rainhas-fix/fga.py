from rainhas import Rainhas
from operator import add
from functools import reduce
import random
from math import floor


class FGA:
    def __init__(self, npop, nRainhas_tabuleiro):
        self.npop = npop
        self.popinicial = [
            Rainhas(nRainhas_tabuleiro) for v in range(npop)]

        for i in self.popinicial:
            i.definir_posicoes_rainha()

    def __len__(self):
        return len(self.popinicial)

    def __setitem__(self, j, val):
        self.popinicial[j] = val

    def __getitem__(self, j):
        return self.popinicial[j]

    def __str__(self):
        return str([r.lista_Rainhas for r in self.popinicial])

    @staticmethod
    def ordena_lista(pop):
        list_elite = pop[:]
        list_elite.sort(key=lambda r: r.colisao())
        return list_elite

    @staticmethod
    def elitizacao(pop, elite):
        return [rainha for rainha in pop][0:elite]

    @staticmethod
    def soma_avaliacoes(pop):
        cont = 0

        for rainha in pop:
            if rainha.avaliacao() == None:
                return rainha

            cont += rainha.avaliacao()
        return cont

    @staticmethod
    def roleta(pop, sum_ava):

        num_aleatorio = random.randrange(0, floor(sum_ava))
        contador = 0

        for posicao, rainha in enumerate(pop):
            contador += rainha.avaliacao()
            if contador > num_aleatorio:
                return rainha


if __name__ == "__main__":
    pass
