n = int(input())
lista = []
for i in range(n):
    lista.append(input())
    
for i in range(1, n):
    current = lista[i]
    position = i
    while position > 0 and len(lista[position - 1]) > len(current):
        lista[position] = lista[position - 1]
        position -= 1
        
    lista[position] = current

if len(lista) >= 2 and len(lista[0]) == len(lista[len(lista) - 1]):
    print('Que mala suerte!')
    
else:
    aux = -1
    ind = len(lista) - 1
    while len(lista[ind]) == len(lista[ind - 1]):
        if len(lista) == 1:
            break
        aux = len(lista[ind])
        lista.pop()
        lista.pop()
        ind -= 2
    
    if len(lista[len(lista) - 1]) == aux:
        lista.pop()
        
    print(lista[len(lista) - 1])
    
# caso de teste que falha

"""
5
Eguinha
Pocotoa
Juanali
Bibi
Ju
"""