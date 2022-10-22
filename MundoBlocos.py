from Estado import *
import random
import gc
            
#Função usada para gerar um estado inicial
def gerar_aleatorio(estado):
    while(len(lista_inicial) > 0):
        y = random.randint(0,2)
        if(y == 0):
            estado.esq.append(lista_inicial.pop(random.randint(0,len(lista_inicial)-1))) #append coloca final da lista
        if(y == 1):
            estado.cent.append(lista_inicial.pop(random.randint(0,len(lista_inicial)-1)))
        if(y == 2):
            estado.dir.append(lista_inicial.pop(random.randint(0,len(lista_inicial)-1)))

def busca_em_largura(obj):
    filhos = []
    while (len(abertos) != 0):
        estado_atual = abertos.pop(0) #estado_atual seria o X

        if(estado_atual.comparaEstado(obj)):
            return "SUCESSO", estado_atual
        else:
            #gerar filhos do X
            filhos.clear()
            gerar_filhos(estado_atual, filhos)

            #colocar X em fechados
            fechados.append(estado_atual)

            #Descartar filhos de X se já estiver em abertos ou fechados
            if( len(filhos) > 0):
                todos_estados = abertos.copy()
                todos_estados.extend(fechados)
                for j in todos_estados:
                    for i in filhos:
                        if(i.comparaEstado(j)):
                            filhos.remove(i)
                #colocar os filhos em abertos
                abertos.extend(filhos)
    return 'FALHA'
    
#Método que gera os filhos a partir de um estado_atual passado via parâmetro
def gerar_filhos(estado_atual, filhos):
    if(estado_atual.get_tam_esq() > 0):
        filho1 = Estado(estado_atual)
        filho1.esq_cent()
        if not estado_atual.comparaEstado(filho1):
            filhos.append(filho1)
        filho2 = Estado(estado_atual)
        filho2.esq_dir()
        if not estado_atual.comparaEstado(filho2):
            filhos.append(filho2)
    
    if(estado_atual.get_tam_cent() > 0):
        filho1 = Estado(estado_atual)
        filho1.cent_esq()
        if not estado_atual.comparaEstado(filho1):
            filhos.append(filho1)
        filho2 = Estado(estado_atual)
        filho2.cent_dir()
        if not estado_atual.comparaEstado(filho2):
            filhos.append(filho2)

    if(estado_atual.get_tam_dir() > 0):
        filho1 = Estado(estado_atual)
        filho1.dir_esq()
        if not estado_atual.comparaEstado(filho1):
            filhos.append(filho1)
        filho2 = Estado(estado_atual)
        filho2.dir_cent()
        if not estado_atual.comparaEstado(filho2):
            filhos.append(filho2)

def caminho(estado_encontrado):
    x = estado_encontrado.pai
    camin=[]
    while (x.pai != None):
        camin.append(x)
        x = x.pai
    camin.append(x)
    return camin


## Inicio do Programa
lista_inicial = ['A', 'B', 'C']
abertos = []
fechados = []
todos_estados = []
estadoInicial = Estado() #estado inicial (aleatorio)
gerar_aleatorio(estadoInicial)
abertos.append(estadoInicial)

#Objetivo Final
obj = Estado()
obj.cent.append('C')
obj.cent.append('B')
obj.cent.append('A')

fim_busca = busca_em_largura(obj)
camin=[]
if(fim_busca[0] == 'SUCESSO'):
    print()
    print(f'Mundo dos Blocos - Daniel Minoru & Samuel Piasecki')
    print()
    print(f'Abertos: {len(abertos)}')
    print(f'Fechados: {len(fechados)}')
    print(f'{fim_busca[0]}')
    camin=caminho(fim_busca[1])
    camin.reverse()
    for x in camin:
        x.print_estado()
    obj.print_estado()
else:
    print(f'{fim_busca[0]}')
