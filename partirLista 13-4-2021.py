


def partirLista(lista):
    if(isinstance(lista,list)):
        if(lista==[])==False:
            return partirLista_aux(lista,[],[])
        else:
            print([])
    else:
        return "error"

def partirLista_aux(lista,result,res):
    if(lista==[]):
        return [result,res]
    elif(lista[0]==lista[-1]):
        return partirLista_aux(lista[1:],result,res+[lista[0]])
    elif(lista[0]>0):
        suma=lista[0]
        return partirLista_aux(lista[1:],result+[suma],res)
    else:
        return partirLista_aux(lista[2:],result,res+[lista[1]])

def partirLista1(lista):
    if(isinstance(lista,list)):
        if(lista==[])==False:
            return partirLista1_aux(lista,[],[])
        else:
            print([])
    else:
        return "error"

def partirLista1_aux(lista,sublista,result):
    if(lista==[]):
        return result+[sublista]
    elif(lista[0]>0):
        suma=lista[0]
        return partirLista1_aux(lista[1:],sublista+[suma],result)
    else:
        return partirLista1_aux(lista[1:],[],result+[sublista])


def partirLista2(lista):
    if(isinstance(lista,list)):
        if(lista==[])==False:
            return partirLista2_aux(lista,[],[],[])
        else:
            print([])
    else:
        return "error"

def partirLista2_aux(lista,sublista,sublista2,result):
    if(lista==[]):
        return result+[sublista]+[sublista2]
    elif(lista[0]>0):
        suma=lista[0]
        return partirLista2_aux(lista[1:],sublista+[suma],sublista2,result)
    else:
        return partirLista2_aux(lista[1:],[],sublista2+[lista[0]],result+[sublista])


#-----------------------------------------------------------------------------------------
"""
funcion de cola
"""
def digitoMayor(num):
    if(isinstance(num,int)):
       if(num>0)and num<10:
           return num
       else:
            return digitomayor_aux(num,0)
    else:
        return "error"

def digitomayor_aux(num,result):
    if(num==0):
        return result
    elif(num%10>result):
        result=num%10
        return digitomayor_aux(num//10,result)
    else:
        return digitomayor_aux(num//10,result)
