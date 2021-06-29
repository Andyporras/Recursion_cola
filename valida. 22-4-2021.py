def valida(lista):
    if(isinstance(lista,list)):
        return valida_aux(lista)
    else:
        return "Error,no es una lista"

def valida_aux(lista):
    if(lista==[]):
        return True
    elif(isinstance(lista[0],int)):
        return valida_aux(lista[1:])
    else:
        return False

# en esta funcion debe almacenar la cantidad.
def tamaño(lista,lista2):
    if(lista==[])or lista2==[]:
        if(lista==[] and lista2==[]):
            return True
        else:
            return False
    else:
        return tamaño(lista[1:],lista2[1:])

def sumaVectores(lista1,lista2):
    verificar=valida(lista1)
    verificar2=valida(lista2)
    if(verificar):
        if(verificar2):
            verificar3=tamaño(lista1,lista2)
            if(verificar3):
                return sumaVectores_aux(lista1,lista2,[])
            else:
                return "Error"
        else:
            return "Error"
    else:
        return "Error"

def sumaVectores_aux(lista1,lista2,result):
    if(lista1==[]):
        return result
    else:
        suma=lista1[0]+lista2[0]
        return sumaVectores_aux(lista1[1:],lista2[1:],result+[suma])


#-------------------------------------------------------------------------------

def restaVectores(lista1,lista2):
    verificar=valida(lista1)
    verificar2=valida(lista2)
    if(verificar):
        if(verificar2):
            verificar3=tamaño(lista1,lista2)
            if(verificar3):
                return restaVectores_aux(lista1,lista2,[])
            else:
                return "Error"
        else:
            return "Error"
    else:
        return "Error"

def restaVectores_aux(lista1,lista2,result):
    if(lista1==[]):
        return result
    else:
        resta=lista1[0]-lista2[0]
        return restaVectores_aux(lista1[1:],lista2[1:],result+[resta])

#------------------------------------------------------------------------------
    

def escalarVectores(lista1,lista2):
    verificar=valida(lista1)
    verificar2=valida(lista2)
    if(verificar):
        if(verificar2):
            verificar3=tamaño(lista1,lista2)
            if(verificar3):
                return escalarVectores_aux(lista1,lista2,0)
            else:
                return "Error"
        else:
            return "Error"
    else:
        return "Error"

def escalarVectores_aux(lista1,lista2,result):
    if(lista1==[]):
        return result
    else:
        suma=lista1[0]*lista2[0]
        return escalarVectores_aux(lista1[1:],lista2[1:],result+suma)

