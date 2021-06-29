def mayorDeLista(lista):
    if(lista==[]):
        return "error"
    else:
        return mayorLista_aux(lista[1:],lista[0])

def mayorLista_aux(lista,resultado):
    if(lista==[]):
        return resultado
    elif(lista[0]>resultado):
        return mayorLista_aux(lista[1:],lista[0])
    else:
        return mayorLista_aux(lista[1:],resultado)
    
def multiplicarElemento():
    if():
        return
    else:
        return


def devolverIndices(lista1,lista2):
    if(lista1==[])and lista2==[]:
        return "error"
    else:
        return devolverIndice_aux(mayor(lista1,lista2),menor(lista1,lista2),[],0)

def mayor(a,b):
    cantidad=len(a)
    cantidad2=len(b)
    if(cantidad>cantidad):
        return a
    else:
        return b
def menor(a,b):
    cantidad=len(a)
    cantidad2=len(b)
    if(b<a):
        return b
    else:
        return a

    
def devolverIndice_aux(lista1,lista2,indice,contador):
    if(lista1==[]):
        return indice
    elif((lista1[0]) in lista2):
        return devolverIndice_aux(lista1[1:],lista2,indice+[contador],contador+1)
    else:
        return devolverIndice_aux(lista1[1:],lista2,indice,contador+1)
    
                              
