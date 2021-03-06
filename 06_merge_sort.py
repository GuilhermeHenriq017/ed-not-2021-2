#   ALGORITMO DE ORDENAÇÃO MERGE SORT
#
#   No processo de ordenação, esse algoritmo "desmonta" o vetor original
#   contendo N elementos até obter N vetores de apenas um elemento cada um.
#   Em seguida, usando a técnica de mesclagem (merge), "remonta" o vetor,
#   dessa vez com os elementos já em ordem.

comps = 0
divisoes = 0
juncoes = 0

def merge_sort(lista):
    """
        Função que implementa o algoritmo merge sort usando o
        método RECURSIVO
    """

    # Não podemos zerar as variáveis globais de estatística
    # dentro da função porque ela é recursiva e resetaria
    # a contagem a cada chamada
    global comps, divisoes, juncoes

    # print(f'Lista recebida: {lista}')

    # Só continua se a lista tiver mais de um elemento
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    # Gera cópia da primeira metade da lista
    lista_esq = lista[:meio]    # Do início ao meio - 1
    # Gera cópia da segunda metade da lista
    lista_dir = lista[meio:]    # Do meio ao 
    
    divisoes += 1

    # Chamamos recursivamente a função para continuar
    # repartindo a lista em metades
    lista_esq = merge_sort(lista_esq)
    lista_dir = merge_sort(lista_dir)

    # print(f'>>> lista_esq: {lista_esq}')
    # print(f'>>> lista_dir: {lista_dir}')

    # Junta as duas metades em uma única lista, ordenada
    pos_esq = 0
    pos_dir = 0
    ordenada = []   # Lista vazia

    # Compara os elementos de cada lista entre si e insere na
    # lista ordenada o que for menor
    while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):
        # O elemento que se encontra na lista da esquerda
        # é menor que o que se encontra na lista da direita
        if lista_esq[pos_esq] < lista_dir[pos_dir]:
            ordenada.append(lista_esq[pos_esq])
            pos_esq += 1
        # O contrário
        else:
            ordenada.append(lista_dir[pos_dir])
            pos_dir += 1
        comps += 1

    sobra = None    # A sobra da lista que ficou para trás

    if pos_esq < pos_dir:  # Houve sobra à esquerda
        sobra = lista_esq[pos_esq:]  # Sobra do pos_esq até o final
    else:   # Houve sobra à direita
        sobra = lista_dir[pos_dir:]  # Sobra do pos_dir até o final

    # print(f'>>>> final ordenada: {ordenada + sobra}')

    # Retornamos a lista final ordenada, composta da ordenada + 
    juncoes += 1
    return ordenada + sobra     # "Soma" de duas listas

#################################################################

comps = 0
divisoes = 0
juncoes = 0

nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

nums_ord = merge_sort(nums)

print(nums_ord)

#################################################################

from data.nomes_desord import nomes
from time import time
import tracemalloc
import psutil

comps = 0
divisoes = 0
juncoes = 0

ini = time()
tracemalloc.start()     # Inicia a medição de consumo de memória

nomes_ord = merge_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

print(nomes_ord)
print(f"Tempo: {fim - ini}")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")
print(f"Comparações: {comps}, divisões: {divisoes}, junções: {juncoes}")
print('The CPU usage is: ', psutil.cpu_percent(4))
tracemalloc.stop()      # Finaliza a medição do consumo de memória