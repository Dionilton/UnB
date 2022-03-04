#Implementação do tipo de dado abstrato Fila

class Queue:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


#Funções
    
def crypto(s):
    #implementação de crypto (médio)
    return s

def deYodafy(w):
    #implementção de deYodafy (fácil)
    return w
    
def merge(i):
    #implementação de merge (médio)
    return i
    
#Programa principal
    
processos = Queue()

while True:
    comando = input().split()
    
    if comando[0] == 'halt':
        n = processos.size()
        print(f'{n} processo(s) e {n} comando(s) órfão(s).')
        break
    
    elif comando[0] == 'add':
        for i in range(int(comando[1])):
            processo = input().split()
            processos.enqueue(processo)
            
    elif comando[0] == 'process':
        processo = processos.dequeue()
        
        if processo[0] == 'crypto':
            print(crypto(processo[1]))
            
        elif processo[0] == 'deYodafy':
            print(deYodafy(processo[1: ]))
            
        elif processo[0] == 'merge':
            print(merge(processo[1: ]))
            
