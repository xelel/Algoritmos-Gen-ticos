from zakharov import Zakharov
from operator import add
import random
from math import floor


class FGA:
    def __init__(self, npop, nZkrv_tabuleiro):
        self.npop = npop
        self.popinicial = [
            Zakharov(nZkrv_tabuleiro) for v in range(npop)]

        for i in self.popinicial:
            i.definir_entradas_aleatorias()

    def __len__(self):
        return len(self.popinicial)

    def __setitem__(self, j, val):
        self.popinicial[j] = val

    def __getitem__(self, j):
        return self.popinicial[j]

    def __str__(self):
        return str([r for r in self])

    @staticmethod
    def ordena_lista(pop):
        list_elite = pop[:]

        list_elite.sort(key=lambda r: r.avaliacao())
        return list_elite

    @staticmethod
    def elitizacao(pop, elite):
        return [zkrv for zkrv in pop][0:elite]

    @staticmethod
    def soma_avaliacoes(pop):
        cont = 0

        for zkrv in pop:
            if zkrv.avaliacao() == None:
                return zkrv

            cont += zkrv.avaliacao()
        return cont

    @staticmethod
    def roleta(pop, sum_ava):

        num_aleatorio = random.randrange(0, floor(sum_ava))
        contador = 0

        for posicao, zkrv in enumerate(pop):
            contador += zkrv.avaliacao()
            if contador > num_aleatorio:
                return zkrv


if __name__ == "__main__":
    f = FGA(2, 8)
    print(f.ordena_lista(f))
    print(f.roleta(f, f.soma_avaliacoes(f)))
