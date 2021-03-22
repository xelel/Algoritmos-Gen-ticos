from abc import abstractmethod
from random import randint, sample, choices, shuffle, choice, randrange
from individuo import Individuo
from itertools import count


class Rainhas(Individuo):
    # Numero de rainhas por tabuleiro(individuo)=n
    def __init__(self, n):
        self.n = n
        # inicializando um array de 0 com dimensão n
        self.lista_Rainhas = [0]*n
        self.aval = None

    # define a posição das rainhas no tabuleiro de forma aleatória
    def definir_posicoes_rainha(self):
        """a função random.sample cria uma lista aleatória, sem elementos repetidos, após receber dois argumentos:
          uma lista ou neste caso um range na qual os números serão escolhidos, e a dimensão da lista."""
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

    # recombinação
    def __add__(self, element):
        """
        Primeiramente é realizado um corte aleatório nos dois pais selecionados.
        O filho 1 recebe a cabeça do pai 1 e a calda do pai2. Quando recebe a calda do pai 2, os valores repetidos recebidos
        do pai 1 ficam com uma marca.
        As posições marcadas como valores repetidos são preenchidas com os valores faltantes de forma aleatória 
        Filho 2 recebe a cabeça do pai 2 e a calda do pai 1 e repete o processo

        """
        if len(self) != len(element):
            # retorno de erro caso o tamanho das rainhas sejam diferentes.
            raise ValueError('os vetores de rainhas devem ter tamanhos iguais')

        # posição na qual o corte será realizado
        corte = randrange(0, len(self)-1)

        # inicializa filho
        filho = Rainhas(self.n)

        # cria um filho, com base na posicao do corte gerado
        filho.lista_Rainhas = self[0:corte] + element[corte:self.n]
        indice_repetido = []

        # procura indice de rainhas repetidas no pai 1 e adiciona em uma lista
        # Percorre o pai 1 e conta quantas vezes o elemento i ocorre na lista
        for i in filho.lista_Rainhas[0:corte]:

            try:

                if filho.lista_Rainhas.count(i) > 1:
                    # Caso o número de rainhas repetidas seja maior que 1 adiciona o indice repetido encontrado na lista indice_repetido
                    indice_repetido.append(filho.lista_Rainhas.index(
                        i, corte, self.n))
            # Caso nenhum valor repetido seja encontrado, um erro é retornado e o loop interrompido
            except ValueError:
                return
        # cria uma lista de Numeros que estão faltando no vetor de rainhas com List comprehension
        num_faltantes = [n for n in range(
            1, len(self)+1) if n not in filho.lista_Rainhas]

        # mistura os numeros faltantes utilizando random.sample
        num_faltantes = sample(num_faltantes, len(num_faltantes))
        # pega o indice do valor repetido e coloca o valor faltante de posição pos
        for pos, indice in enumerate(indice_repetido):
            filho.lista_Rainhas[indice] = num_faltantes[pos]

        return filho

    def avaliacao(self):
        """
        Avaliação do individuo = 1/avaliação por ser um problema de minimização
        """
        try:
            self.aval = (1/self.colisao())
            return self.aval
        except(ZeroDivisionError):
            return

    # colisao entre rainhas
    def colisao(self):
        """ conta o número de colisões entre rainhas que ocorrem no tabuleiro(individuo)        
        """
        contador = 0
        # Percorre o tabuleiro
        for i in range(len(self)):
            for j in range(1+i, len(self)):
                if self.lista_Rainhas[i] == self.lista_Rainhas[j]+abs(i-j):
                    contador += 1
                elif self.lista_Rainhas[i] == self.lista_Rainhas[j]-abs(i-j):
                    contador += 1
        return contador

    def mutar(self):
        """ 
        O mutante recebe todos os genes do pai.
        Sorteia-se dois genes para troca de valores.

        """
        rainhas_aleatorias = sample(self.lista_Rainhas, 2)
        # r_1= gene 1
        # r_2 = gene 2
        r_1, r_2 = rainhas_aleatorias
        pos_r_1 = self.lista_Rainhas.index(r_1)  # armazena a posição do gene 1
        pos_r_2 = self.lista_Rainhas.index(r_2)  # armazena a posição do gene 2

        # realiza a troca dos genes de posição pos_r_1 e pos_r_2
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
