def devolverIndice(lista,valor):
    if(lista==[]):
        return "Error"
    else:
        return indice(lista,valor,0,[])

def indice(lista,valor,indiceActual,indiceAnterior):
    if(lista==[]):
        return []
    elif(isinstance(lista[0],list)):
        return indice(lista[0],valor,0,indiceAnterior+[indiceActual])
    else:
        if(lista[0]==valor):
            return indiceAnterior+[indiceActual]
        else:
            return indice(lista[1:],valor,indiceActual+1,indiceAnterior)
