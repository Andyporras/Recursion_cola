"""
clase del dia 6-4-2021 introduccion 
"""

def contarrDigito(num):
    if(isinstance(num,int)and num>0):
        return contar_aux(num,0)
    else:
        print("digite un numero entero positivo mayor a cero")

def contar_aux(num,contar):
    if(num==0):
        return contar
    else:
        return contar_aux(num//10,contar+1)

def sumatoriaIntervalo(inicio,fin):
    if(isinstance(inicio,int)and isinstance(fin,int)and inicio>0 and fin>inicio):
        return sumatoria_aux(inicio,fin,0)
    else:
        print("digite un numero entero positivo y el inicio debe ser mayor al final")

def sumatoria_aux(inicio,fin,result):
    if(inicio>fin):
        return result
    else:
        return sumatoria_aux(inicio+1,fin,result+inicio)




def multiplicacion(num):
    if(isinstance(num,int) and num>0):
       return multiplicacion_aux(num,1)
    else:
        print("error,digite un numero entero positivo")

def multiplicacion_aux(num,result):
    if(num==0):
        return result
    elif(num%10)%5==0 or (num%10)%3==0:
        return multiplicacion_aux(num//10,result*(num%10))
    else:
        return multiplicacion_aux(num//10,result)
