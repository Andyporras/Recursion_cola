def devolverIndices2(lista1,lista2):
    if(lista1==[]) and lista2==[]:
        return ""
    else:
        return devolverIndice_aux(lista1,lista2,[])

def obtenerIndice(lista1,elemento,indice,resultado):
    if(lista1==[]):
        return resultado
    elif(lista1[0]==elemento):
        resultado=indice
        return obtenerIndice(lista1[1:],elemento,indice+1,resultado+1)
    else:
        return obtenerIndice(lista1[1:],elemento,indice+1,resultado)

def devolverIndice_aux(lista,lista2,resultado):
    if(lista2==[]):
        return resultado
    else:
        indice=obtenerIndice(lista,lista2[0],-1,-1)
        if(indice!=-1):
            resultado+=[indice]
            return devolverIndice_aux(lista,lista2[1:],resultado)
        else:
            return devolverIndice_aux(lista,lista2[1:],resultado)
