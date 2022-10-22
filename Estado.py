class Estado (object):
    def __init__(self, pai=None):
        if(pai != None):
            self.esq = pai.esq.copy()
            self.cent = pai.cent.copy()
            self.dir = pai.dir.copy()
        else:
            self.esq = []
            self.cent = []
            self.dir = []
        self.pai = pai

    def copy(self ,estado_filho):
        estado_filho.esq = self.esq.copy()
        estado_filho.cent = self.cent.copy()
        estado_filho.dir = self.dir.copy()

    #retorna tamanho da pilha esq
    def get_tam_esq(self):
        return len(self.esq)   
        
    #retorna tamanho da pilha cent
    def get_tam_cent(self):
        return len(self.cent)   

    #retorna tamanho da pilha dir
    def get_tam_dir(self):
        return len(self.dir)                    

    #Retira elemento da pilha esq e adiciona no topo da pilha cent
    def esq_cent(self):
        if (self.get_tam_esq() > 0):
            self.cent.append(self.esq.pop())

    #Retira elemento da pilha esq e adiciona no topo da pilha dir 
    def esq_dir(self):    
        if (self.get_tam_esq() > 0):
            self.dir.append(self.esq.pop())            

    #Retira elemento da pilha cent e adiciona no topo pilha esq 
    def cent_esq(self):      
        if (self.get_tam_cent() > 0):
            self.esq.append(self.cent.pop())

    #Retira elemento da pilha cent e adiciona no topo pilha dir
    def cent_dir(self):
        if (self.get_tam_cent() > 0):
            self.dir.append(self.cent.pop())
        
    #Retira elemento da pilha dir e adiciona no topo pilha esq  
    def dir_esq(self):  
        if (self.get_tam_dir() > 0):
            self.esq.append(self.dir.pop())            

    #Retira elemento da pilha dir e adiciona no topo pilha cent
    def dir_cent(self):      
        if (self.get_tam_dir() > 0):
            self.cent.append(self.dir.pop())            

    #Compara o conteúdo de duas pilhas quaisquer sabendo que ambos tem a mesma quantidade de elementos
    def comparaPilha(self, pilha1, pilha2):
        for i in range(len(pilha1)):
            if(pilha1[i] != pilha2[i]):
                return False
        return True   

    def comparaEstado(self, outro_estado):
        if((len(self.esq) != len(outro_estado.esq))
        or (len(self.cent) != len(outro_estado.cent))
        or (len(self.dir) != len(outro_estado.dir))):
            return False 
        if(len(self.esq) == len(outro_estado.esq)):
            if not self.comparaPilha(self.esq, outro_estado.esq):
                return False
        if(len(self.cent) == len(outro_estado.cent)):
            if not self.comparaPilha(self.cent, outro_estado.cent):
                return False
        if(len(self.dir) == len(outro_estado.dir)):
            if not self.comparaPilha(self.dir, outro_estado.dir):
                return False   
        return True   

    def maximo_blocos(self):
        return 3

    def print_estado(self):
        print(f'\n---------')
        for i in reversed(range(self.maximo_blocos())):
            if(i >= len(self.esq)):
                print(f' ', end=" ")
            else:
                print(f'{self.esq[i]}', end=" ")

            if(i >= len(self.cent)):
                print(f' ', end=" ")
            else:
                print(f'{self.cent[i]}', end=" ")

            if(i >= len(self.dir)):
                print(f' ', end=" ")
            else:
                print(f'{self.dir[i]}', end=" ")
            print()
        print(f'1-2-3') 