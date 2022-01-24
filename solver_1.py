#
# Posição variando de 0 à 4
#

#
# As três melhores palavras para começar, com a somarória das frequências das letras nas palavras ao lado são:
#
# rosea 52.27
# serao 52.269999999999996
# anoes 50.790000000000006
#

import csv
from functools import reduce

print("Lembre-se: posições no python são dadas de 0 à 4")


#
# Importação dos dados .csv e armazenamento dos mesmos numa lista chamada armazena.
#

file = open('dados_filtrados.csv')
csvreader = csv.reader(file)
armazena = []
for row in csvreader:
    armazena.append(row[0])

#
# Dicionário contendo a frequência de cada letra nas palavras da língua portuguesa. 
#

dic_letras = {'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99, 'e': 12.57, 'f': 1.02, 'g': 1.30, 'h': 1.28, 'i': 6.18, 'j': 0.40, 'k': 0.02, 'l': 2.78, 'm': 4.74, 'n': 5.05, 'o': 10.73, 'p': 2.52, 'q': 1.20, 'r': 6.53, 's': 7.81, 't': 4.34, 'u': 4.63, 'v': 1.67, 'w': 0.01, 'x': 0.21, 'y': 0.01, 'z': 0.47}

n_acertos_verdes_totais = 0
n_acertos_amarelos_totais = 0
n_acertos_vermelhos_totais = 0

lista_acerto_verde = [[None, None], [None, None], [None, None], [None, None], [None, None]]
lista_acerto_amarelo = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
lista_acerto_vermelho = [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]]

#
# Inputs do usuário.
#

for i in range(5): 
    n_acertos_verdes = int(input("Insira o número de acertos verdes da rodada: "))
    n_acertos_amarelos = int(input("Insira o número de acertos amarelos da rodada: "))
    n_acertos_vermelhos = int(input("Insira o número de acertos vermelhos da rodada: "))
    
    for i in range(n_acertos_verdes):
        lista_acerto_verde[n_acertos_verdes_totais +i][0] = input("Insira uma letra verde acertada: ")
        lista_acerto_verde[n_acertos_verdes_totais +i][1] = int(input("Insira a posição da letra verde acertada dada anteriormente: "))
                                                             
    for i in range(n_acertos_amarelos):
        lista_acerto_amarelo[n_acertos_amarelos_totais +i][0] = input("Insira uma letra amarela acertada: ")
        lista_acerto_amarelo[n_acertos_amarelos_totais +i][1] = int(input("Insira a posição da letra amarela acertada dada anteriormente: "))
        
    for i in range(n_acertos_vermelhos):
        lista_acerto_vermelho[n_acertos_vermelhos_totais +i] = input("Insira a letra em vermelho acertada: ")
    
#
# Filtro Verde
#

    armazena_verde = []

    for i in range(n_acertos_verdes):
        armazena_verde.append([])
        letra = lista_acerto_verde[n_acertos_verdes_totais +i][0]
        posicao =  lista_acerto_verde[n_acertos_verdes_totais +i][1]
        for j in armazena:
            if letra == j[posicao]:
                armazena_verde[i].append(j)
    if n_acertos_verdes != 0:
        armazena = list(reduce(set.intersection, [set(x) for x in armazena_verde]))
#   
# Filtro amarelo
#

    armazena_amarelo = []

    for i in range(n_acertos_amarelos):
        armazena_amarelo.append([])
        letra = lista_acerto_amarelo[n_acertos_amarelos_totais +i][0]
        posicao =  lista_acerto_amarelo[n_acertos_amarelos_totais +i][1]
        for j in armazena:
            if letra in j and letra != j[posicao]:
                armazena_amarelo[i].append(j)    
    if n_acertos_amarelos != 0:
        armazena = list(reduce(set.intersection, [set(x) for x in armazena_amarelo]))

#    
# Filtro vermelho
#

    armazena_vermelho = []

    for i in range(n_acertos_vermelhos):
        armazena_vermelho.append([])
        letra = lista_acerto_vermelho[n_acertos_vermelhos_totais +i]
        for j in armazena:
            if letra not in j:
                armazena_vermelho[i].append(j)    
    if n_acertos_vermelhos != 0:
        armazena = list(reduce(set.intersection, [set(x) for x in armazena_vermelho]))
    
    n_acertos_verdes_totais = n_acertos_verdes_totais + n_acertos_verdes
    n_acertos_amarelos_totais = n_acertos_amarelos_totais + n_acertos_amarelos
    n_acertos_vermelhos_totais = n_acertos_vermelhos_totais + n_acertos_vermelhos

#    
# Atribuições da soma da frequencia de cada letra na lingua portuguesa à cada palavra na lista armazena.
#

    dic_palavras = {}

    for i in armazena:
        dic_palavras[i] = 0
        dic_condicao = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w':0, 'x': 0, 'y': 0, 'z': 0}
        for j in i:
            for k in dic_letras:
                if j == k and dic_condicao[j] != 1:
                    dic_palavras[i] +=  dic_letras[k]
                    dic_condicao[j] = 1 # Só vai contar a letra uma única vez
                    
                    
    print("Segue abaixo e uma lista com todas as palavras possíveis, seguida pela soma das frequências de cada letra da palavra, em ordem decrescente. ")
    for i in sorted(dic_palavras, key = dic_palavras.get, reverse=True):
        print(i, dic_palavras[i])
    print("########################### Fim da iteração #############################################")
        

                
            
    
            