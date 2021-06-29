def sumaVectores(vector1,vector2):
    if(isinstance(vector1,list)and isinstance(vector2,list)):
       if(valida_aux(vector1)):
           if(valida_aux(vector2)):
               if(tamaño(vector1,0))==((tamaño(vector2,0))):
                   return sumaVectores_aux(vector1,vector2,[])
                else:
                    return "Error,no tiene el mismo tamaño"
            else:
                return "Error"
        else:
            return "Error"
    else:
        return "error"


def sumaVectores_aux(vector1,vector2,result):
    if(vector1==[]):
        return result
    else:
        if(tamaño(vector1,0))>1:
            return sumaVectores_aux(vector1[2:],vector2[2:],result+[vector1[1]+vector2[1]])
        else:
            return result


def valida_aux(lista):
    if(lista==[]):
        return True
    elif(isinstance(lista[0],int)):
        return valida_aux(lista[1:])
    else:
        return False


def tamaño(lista,cont):
    if(lista==[]):
        return cont
    else:
        return tamaño(lista[1:],cont+1)

