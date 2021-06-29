def sumarMatrizInferior(m):
    if(isinstance(m,list)and m!=[]):
        if(verificar_aux(m)):
           if(tamaño(m)):
              if(len(m))>2:
                  if(len(m)%2)==0:
                      return sumaColumnas_aux2(m,(len(m)//2),len(m),0,len(m[0]),0,[])
                  else:
                      return sumaColumnas_aux3(m,(len(m)//2)+1,len(m),0,len(m[0]),0,[])
              else:
                  return "error, debe tener la matriz mas de 2 lista"
           else:
               return "error,debe ingresar "

def tamaño(m):
    return tamaño_aux(m,1)
def tamaño_aux(m,indice):
    if(len(m))==1:
        return True
    elif(len(m[0]))==len(m[indice]):
        return tamaño_aux(m[1:],indice)
    else:
        return False

def verificar_aux(m):
    if(m==[]):
        return True
    elif(isinstance(m[0],list)):
        if(verificar_entero(m[0])):
            return verificar_aux(m[1:])
        else:
            return False
    else:
        return False
def verificar_entero(m):
    if(m==[]):
        return True
    elif(isinstance(m[0],int)):
        return verificar_entero(m[1:])
    else:
        return False


def sumaColumnas_aux2(m,fila_actual,m_filas,columna_actual,n_columnas,suma_columna,result):
    if(columna_actual==n_columnas):
        return result
    elif(fila_actual==m_filas):
        return sumaColumnas_aux2(m,(len(m)//2),m_filas,columna_actual+1,n_columnas,0,result+[suma_columna])
    else:
        suma_columna+=m[fila_actual][columna_actual]
        return sumaColumnas_aux2(m,fila_actual+1,m_filas,columna_actual,n_columnas,suma_columna,result)

        
def sumaColumnas_aux3(m,fila_actual,m_filas,columna_actual,n_columnas,suma_columna,result):
    if(columna_actual==n_columnas):
        return result
    elif(fila_actual==m_filas):
        return sumaColumnas_aux3(m,(len(m)//2),m_filas,columna_actual+1,n_columnas,0,result+[suma_columna])
    else:
       # print(m[fila_actual][columna_actual])
        suma_columna+=m[fila_actual][columna_actual]
        return sumaColumnas_aux3(m,fila_actual+1,m_filas,columna_actual,n_columnas,suma_columna,result)
    
#--------------------------------------------------------------------------------------------------------------------

def sumarMatrizDerecha(m):
    if(isinstance(m,list)and m!=[]):
        if(verificar_aux(m)):
           if(tamaño(m)):
               if(len(m[0]))%2==0:
                   return sumaColumnas1_aux(m,0,len(m),(len(m[0])//2),len(m[0]),0,[])
               else:
                   return sumaColumnas1_aux(m,0,len(m),((len(m[0])//2)),len(m[0]),0,[])

    

def sumaColumnas1_aux(m,fila_actual,m_filas,columna_actual,n_columnas,suma_columna,result):
    if(columna_actual==n_columnas):
        return result
    elif(fila_actual==m_filas):
        return sumaColumnas1_aux(m,0,m_filas,columna_actual+1,n_columnas,0,result+[suma_columna])
    else:
        suma_columna+=m[fila_actual][columna_actual]
        return sumaColumnas1_aux(m,fila_actual+1,m_filas,columna_actual,n_columnas,suma_columna,result)

"""       
def sumaColumnas2_aux(m,fila_actual,m_filas,columna_actual,n_columnas,suma_columna,result):
    if(columna_actual==n_columnas):
        return result
    elif(fila_actual==m_filas):
        return sumaColumnas2_aux(m,0,m_filas,columna_actual+1,n_columnas,0,result+[suma_columna])
    else:
        suma_columna+=m[fila_actual][columna_actual]
        return sumaColumnas2_aux(m,fila_actual+1,m_filas,columna_actual,n_columnas,suma_columna,result)      
"""
