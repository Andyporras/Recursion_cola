def contarDigitosDivisores(num, divisor):
    if isinstance(num,int) and isinstance(divisor,int):
        if(divisor > 0 and divisor < 10):
            return aux(num, divisor,0)
        else:
            return 'num y divisor deben de ser enteros'

def aux(num, divisor,result):
    if(num == 0):
        return result
    else:
        if((num%10)%divisor==0):
            return aux(num//10,divisor,result+1)
        else:
            return aux(num//10,divisor,result)
        

def adyacetes(num):
    if(num>0):
        return sumaDeImpares(num,0,0,True)
        
            
    else:
        print("")

def sumaDeImpares(num,suma,contador,result):
    if(num==0):
        return result
    elif(contador==2)and suma%2==1 and result!= False:
        return sumaDeImpares(num,suma-suma,contador-2,True)
    elif(contador==2):
        return False
    else:
        return sumaDeImpares(num//10,suma+(num%10),contador+1,result)


def lista(lista):
    if(lista==[]):
        return "Error"
    else:
        if(isinstance(lista,list)):
            return parImpar(lista,[],[])
        else:
            return ""

def parImpar(lista,par,impar):
    if(lista==[]):
        result=[par]+[impar]
        return result
    elif(lista[0]%2==0):
        return parImpar(lista[1:],par+[lista[0]],impar)
    else:
        return parImpar(lista[1:],par,impar+[lista[0]])

            
