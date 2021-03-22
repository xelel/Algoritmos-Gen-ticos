from fga import FGA
from itertools import count
from rainhas import Rainhas

npop = int(input('Digite a população inicial de indivíduos: '))
nRainhas = 12
nGeracoes = int(input('Digite o número máximo de gerações: '))
nElite = 2

# cria uma populacao inicial com n_rainhas por individuo
f = FGA(npop=npop, nRainhas_tabuleiro=nRainhas)
contador = 1


pop_atual = f.popinicial

# laço no range com  número de gerações passadas
for geracao in range(0, nGeracoes):
    parada = None
    # Caso não houver colisões no tabuleiro o laço é interropido, retornando o individuo e a geração atual.
    for r in pop_atual:
        if r.colisao() == 0:
            print(
                f'Tabuleiro de rainhas sem colisoes encontrado {r} {r.colisao()} em {contador} gerações')
            parada = True
            break
    if parada:
        break
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

    # percorre a populacao de filhos, e verifica se algum tabuleiro sem colisão foi encontrado.
    # Se tiver algum filho sem colisões o laço é interrompido
    for r in lista_filhos:
        if r.colisao() == 0:
            print(
                f'Rainha sem colisoes encontrada {r} {r.colisao()} em {contador} gerações')
            parada = True
            break

    if parada:
        break

    # Cria uma populacao de individuos mutantes com list comprehension
    lista_mutantes = [Rainhas.mutar(mutante) for mutante in pop_atual]

    # Verifica novamente, se algum individuo sem colisoes foi encontrado.
    for r in lista_mutantes:
        if r.colisao() == 0:
            print(
                f'Rainha sem colisoes encontrada {r} {r.colisao()} em {contador} gerações')
            parada = True
            break
    if parada:
        break
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

    except:  # caso um erro seja retornado, a condição de parada foi encontrada e o laço é parado.

        print(
            f'Rainha sem colisoes encontrada {r} {r.colisao()} em {contador} gerações')
        break
    # Caso a condição de parada não seja satisfeita, passa para a próxima geração
    # a população atual = a elite + os indiviudos selecionados na roleta
    pop_atual = elite + individuos_roleta
    contador += 1
