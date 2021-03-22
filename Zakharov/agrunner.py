from fga import FGA
from itertools import count
from zakharov import Zakharov

npop = int(input('Digite a população de indivíduos inicial: '))
nZakharov = int(
    input('Digite a dimensão(d) da função(número de genes por indivíduo): '))
nGeracoes = int(input('Digite o número máximo de gerações: '))
nElite = 2

# Inicializa uma população inicial com npop:população inicial, e nZakharov: Número de genes por indivíduos
f = FGA(npop=npop, nZkrv_tabuleiro=nZakharov)
contador = 1


pop_atual = f.popinicial
melhor_geracao = None

# Itera no valor das geracões passadas como entrada
for geracao in range(0, nGeracoes):
    parada = None
    for z in pop_atual:
        # Inicializa o valor melhor_geração com o valor de z.avaliacao()
        if melhor_geracao == None:
            melhor_geracao = z.avaliacao()
        # Caso a avaliacao da populacao atual seja menor do que a avaliacao da populacao anterior
        # muda o valor de melhor_geracao para z.avaliacao()
        elif z.avaliacao() < melhor_geracao:
            melhor_geracao = z.avaliacao()
        # Caso a condição de parada seja encontrada, o loop é interrompido
        elif z.avaliacao() == 0:
            print(f'condição de parada encontrada {z.melhor_entrada}')

    # lista população intermediária
    pop_intermediaria = []
    # cria uma lista de pais com list comprehension, percorrendo a populacao atual, e criando uma tupla de pais, com os elementos
    # i, i+1, andando de 2 em 2
    lista_pais = [(pai1, pai2)
                  for pai1, pai2 in zip(pop_atual[0::2], pop_atual[1::2])]
    # lista de filhos

    lista_filhos = []
    # realiza a recombinação do pai1 + pai2 e pai2 + pai1, gerando dois filhos
    for i in lista_pais:
        pai1, pai2 = i
        lista_filhos.append(pai1+pai2)
        lista_filhos.append(pai2+pai1)
    # Cria uma populacao de individuos mutantes com list comprehension
    lista_mutantes = [Zakharov.mutar(mutante) for mutante in pop_atual]

    # cria população intermediária, que passará pelo processo de seleção natural(Roleta e elitização)
    pop_intermediaria = pop_atual + lista_filhos + lista_mutantes
    # Ordena a lista com base no número de colisoes encontradas no indivíduo
    pop_intermediaria_ordenada = f.ordena_lista(pop_intermediaria)

    # captura os melhores individuos da população com base no argumento nElite passado
    elite = f.elitizacao(pop_intermediaria_ordenada, nElite)
    # somatório das avaliações da população intermediária
    ava_soma = f.soma_avaliacoes(pop_intermediaria_ordenada)
    # inicializa uma lista de individuos para roleta- o número de individuos selecionados por elitização
    individuos_roleta = [0]*(f.npop-nElite)

    try:
        # laço com range número da população de rainhas- elite
        for l in range(f.npop-nElite):
            # Passa o valor da roleta para o individuo l do laço
            individuos_roleta[l] = f.roleta(
                pop_intermediaria_ordenada, ava_soma)

    except:  # caso um erro seja retornado, a condição de parada foi encontrada e o loop interrompido.
        for z in individuos_roleta:
            if z.avaliacao() < melhor_geracao:
                melhor_geracao = z.avaliacao()
            print(f'condição de parada encontrada ')
            break
   # Caso a condição de parada não seja satisfeita, passa para a próxima geração
    # a população atual = a elite + os indiviudos selecionados na roleta
    pop_atual = elite + individuos_roleta

    for z in pop_atual:
        if z.avaliacao() < melhor_geracao:
            melhor_geracao = z.avaliacao()

    print(f'melhor sáida da geração {contador}:{melhor_geracao}')
    contador += 1
