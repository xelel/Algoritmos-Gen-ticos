from fga import FGA
from itertools import count
from zakharov import Zakharov

npop = int(input('Digite a população de Zakharov: '))
nZakharov = int(input('Digite a dimensão(d) da função: '))
nGeracoes = int(input('Digite o número máximo de gerações: '))
nElite = int(input('Digite nElite: '))


f = FGA(npop=npop, nZkrv_tabuleiro=nZakharov)
contador = 1


pop_atual = f.popinicial
melhor_geracao = None
for geracao in range(0, nGeracoes):
    parada = None
    for z in pop_atual:
        if melhor_geracao == None:
            melhor_geracao = z.avaliacao()
        elif z.avaliacao() < melhor_geracao:
            melhor_geracao = z.avaliacao()
        elif z.avaliacao() == 0:
            print(f'condição de parada encontrada {z.melhor_entrada}')

    pop_intermediaria = []
    lista_pais = [(pai1, pai2)
                  for pai1, pai2 in zip(pop_atual[0::2], pop_atual[1::2])]

    lista_filhos = []

    for i in lista_pais:
        pai1, pai2 = i
        lista_filhos.append(pai1+pai2)
        lista_filhos.append(pai2+pai1)

    lista_mutantes = [Zakharov.mutar(mutante) for mutante in pop_atual]

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
        for z in individuos_roleta:
            if z.avaliacao() < melhor_geracao:
                melhor_geracao = z.avaliacao()
            print(f'condição de parada encontrada ')
            break

    pop_atual = elite + individuos_roleta
    for z in pop_atual:
        if z.avaliacao() < melhor_geracao:
            melhor_geracao = z.avaliacao()

    print(f'melhor sáida da geração {contador}:{melhor_geracao}')
    contador += 1
