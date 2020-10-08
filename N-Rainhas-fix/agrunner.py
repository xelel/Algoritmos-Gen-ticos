from fga import FGA
from itertools import count
from rainhas import Rainhas

npop = int(input('Digite a população de rainhas: '))
nRainhas = int(input('Digite o número de rainhas por tabuleiro: '))
nGeracoes = int(input('Digite o número máximo de gerações: '))
nElite = int(input('Digite nElite: '))

f = FGA(npop=npop, nRainhas_tabuleiro=nRainhas)
contador = 1


pop_atual = f.popinicial

for geracao in range(0, nGeracoes):
    parada = None
    for r in pop_atual:
        if r.colisao() == 0:
            print(
                f'Rainha sem colisoes encontrada {r} {r.colisao()} em {contador} gerações')
            parada = True
            break
    if parada:
        break

    pop_intermediaria = []
    lista_pais = [(pai1, pai2)
                  for pai1, pai2 in zip(pop_atual[0::2], pop_atual[1::2])]

    lista_filhos = []

    for i in lista_pais:
        pai1, pai2 = i
        lista_filhos.append(pai1+pai2)
        lista_filhos.append(pai2+pai1)

    for r in lista_filhos:
        if r.colisao() == 0:
            print(
                f'Rainha sem colisoes encontrada {r} {r.colisao()} em {contador} gerações')
            parada = True
            break

    if parada:
        break

    lista_mutantes = [Rainhas.mutar(mutante) for mutante in pop_atual]

    for r in lista_mutantes:
        if r.colisao() == 0:
            print(
                f'Rainha sem colisoes encontrada {r} {r.colisao()} em {contador} gerações')
            parada = True
            break
    if parada:
        break

    pop_intermediaria = pop_atual + lista_filhos + lista_mutantes
    pop_intermediaria_ordenada = f.ordena_lista(pop_intermediaria)

    elite = f.elitizacao(pop_intermediaria_ordenada, nElite)
    ava_soma = f.soma_avaliacoes(pop_intermediaria_ordenada)
    individuos_roleta = [0]*(f.npop-nElite)

    try:
        for l in range(f.npop-nElite):
            individuos_roleta[l] = f.roleta(
                pop_intermediaria_ordenada, ava_soma)

    except:

        print(
            f'Rainha sem colisoes encontrada {r} {r.colisao()} em {contador} gerações')
        break
    pop_atual = elite + individuos_roleta
    contador += 1
