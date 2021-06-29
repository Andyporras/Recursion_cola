#--------------------------------------------
"""
esta mal este codigo
"""
def esPrimo(num):
    if(isinstance(num,int)and num >0):
        return esPrimo_aux(num,True)
    else:
        return "Error, numero no es entero positivo mayor a cero"

def esPrimo_aux(num,result):
    if(num==0) or result==False:
        return result
    
    elif(num%10%3==0)and num%10 !=6 and num%10!=9:
        return esPrimo_aux(num//10,result)
    elif(num%10%5==0):
        return esPrimo_aux(num//10,result)
    elif(num%10%7==0):
        return esPrimo_aux(num//10,result)
    else:
        return esPrimo_aux(num//10,False)
#------------------------
    


def primo(num):
    if(isinstance(num,int)):
        return primo_aux(num,num//2)

def primo_aux(num,resta):
    if(resta>):
        if(num==1):
            return True
        else:
            return False
    else:
        return primo_aux(num-1,resta+1)
    
#------------------------------------------------------------------------   
    



def listaCapicua(lista):
    if(isinstance(lista,list)):
       if(lista==[]):
           return False
       else:
           num=transformar_a_entero(lista,0,0)
           return listaCapicua_aux(lista,num,0,0)
    else:
        print("error")

def transformar_a_entero(lista,result,contador):
    if(lista==[]):
        return result
    else:
        return transformar_a_entero(lista[:-1],result+(lista[-1]*10**contador),contador+1)
    
def listaCapicua_aux(lista,num,result,cont):
    if(lista==[]):
        if(num==result):
            return True
        else:
            return False
    else:
        return listaCapicua_aux(lista[1:],num,result+(lista[0]*10**cont),cont+1)


#-------------------------------------------------------------------------------------------------------------------


def ordenarLista(lista):
    if(isinstance(lista,list)):
        if(len(lista))>1:
            return ordenarLista_aux(lista,[0])

def ordenarLista_aux(lista,result):
    menor=menor_aux(lista,1000000000000000,int(result[-1]))
    if(len(lista)<(len(result))):
        return print(result[1:])
    else:
        return ordenarLista_aux(lista,result+[menor])
        
        



def menor_aux(lista,result,num):
    if(lista==[]):
        return result
    
    elif(lista[0])<result and num<lista[0]:
        return menor_aux(lista[1:],lista[0],num)
    else:
        return menor_aux(lista[1:],result,num)
        
       
