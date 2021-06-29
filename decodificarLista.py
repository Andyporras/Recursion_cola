def decodificarLista(vector):
    if(isinstance(vector,list)):
        if(isinstance(vector[0],int)):
            if(verificar_aux(vector)):
                entero=entero_aux(vector,0,0)
                return binario_aux([entero],[])
            else:
                return "Error"
        else:
            if(verificar1_aux(vector)):
                if(tamaño_aux(vector[1:],vector[0])):
                    return convertir_aux(vector,[])
                else:
                    return "error,tamaños distintos de los sub lista"
            else:
                return "Error, las sub lista tiene datos distintos a un entero"
    else:
        return print("Error,el dato ingresado no es una lista")

def verificar_aux(vector):
    if(vector==[]):
        return True
    else:
        if(isinstance(vector[0],int)):
            return verificar_aux(vector[1:])
        else:
            return False

def verificar1_aux(vector):
    if(vector==[]):
        return True
    else:
        if(verificar_aux(vector[0])):
            return verificar1_aux(vector[1:])
        else:
            return False

def convertir_aux(lista,result):
    if(lista==[]):
        return binario_aux(result,[])
    else:
        entero=entero_aux(lista[-1],0,0)
        return convertir_aux(lista[:-1],result+[entero])

def tamaño_aux(vector,comparar):
    if(vector==[]):
        return True
    else:
        if(comparar_tamaño(vector[0],0))==(comparar_tamaño(comparar,0)):
            return tamaño_aux(vector[1:],vector[0])
        else:
            return False

def comparar_tamaño(vector,cont):
    if(vector==[]):
        return cont
    else:
        return comparar_tamaño(vector[1:],cont+1)


def entero_aux(lista,result,cont):
    if(lista==[]):
       return result
    else:
        dato=int(lista[-1])
        suma=(dato)*(10**cont)
        return entero_aux(lista[:-1],result+suma,cont+1)
    
    
def binario_aux(lista,result):
    if(lista==[]):
        return result
    else:
        binario=transformar_A_binario(lista[-1],0,0)
        return binario_aux(lista[:-1],result+[binario])

def transformar_A_binario(num,cont,result):
    if(num==0):
        return result
    else:
        result+=((num%2)*(10**cont))
        return transformar_A_binario(num//2,cont+1,result)
