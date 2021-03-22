from rainhas import Rainhas
from operator import add
from functools import reduce
import random
from math import floor


class FGA:
    """
    Inicializa a população, com o número de individuos por população, 
    e o número de genes(rainhas) por individuo
    """

    def __init__(self, npop, nRainhas_tabuleiro):
        self.npop = npop
        # cria uma lista de rainhas com o número de população recebido.
        self.popinicial = [
            Rainhas(nRainhas_tabuleiro) for v in range(npop)]

        # define as posições aleatorias dos individuos
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
        """Ordena a lista recebida como parametro, com base no numero de colisões
            de rainhas no individuo
        """
        list_elite = pop[:]
        list_elite.sort(key=lambda r: r.colisao())
        return list_elite

    @staticmethod
    def elitizacao(pop, elite):
        # Retorna uma lista de rainhas com base no número de elite passado como parametro
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
        """ existem duas formas de fazermos a roleta: uma pra maximização e uma pra minimização. 
            O problema da rainha é um problema de minimização.
            recebe uma populacao ordenada, gera um número aleatório entre 0 e o somátorio da lista de avaliações passado com argumento.
            variável contador = soma da avaliacao dos individuos da população
        """
        num_aleatorio = random.randrange(0, floor(sum_ava))
        contador = 0

        # Percorre a populacao de individuos enquanto a variável contador for menor que a variável num_aleatorio
        # quando a condição for satisfeita, para o laço e retorna a rainha.
        for posicao, rainha in enumerate(pop):
            contador += rainha.avaliacao()
            if contador > num_aleatorio:
                return rainha


if __name__ == "__main__":
    pass
