def multiplicacionDeMatriz(matriz1,matriz2):
    if(isinstance(matriz1,list)and isinstance(matriz2,list)):
        if(verificar_aux(matriz1)):
            if(verificar_aux(matriz2)):
                if(tamaño(matriz1))== tamaño(matriz2):
                    if(tamaño(matriz1)==largo_lista(matriz2,0)):
                        return multiplicarMatriz(matriz1,matriz2,tamaño(matriz1),largo_lista(matriz1,0),0,0,0,[],0,[])
                    else:
                        return "ERROR,"
                else:
                    return "ERROR,"
            else:
                return "ERROR,"
        else:
            return "ERROR,"
    else:
        return "ERROR,"
    
def multiplicarMatriz(matriz1,matriz2,columna,fila,columna_actual,fila_actual,suma,result,cont,result2):
    if(columna_actual==columna):
        return result2
    elif(cont==fila):
        return multiplicarMatriz(matriz1,matriz2,columna,fila,columna_actual+1,0,0,[],0,result2+[result])
    elif(fila_actual==fila):
        return multiplicarMatriz(matriz1,matriz2,columna,fila,columna_actual,0,0,result+[suma],cont+1,result2)
    else:
        #print(matriz1[columna_actual][fila_actual]*matriz2[fila_actual][cont]])
        #print(matriz1[columna_actual][fila_actual],matriz2[fila_actual][cont])
        suma+=matriz1[columna_actual][fila_actual]*matriz2[fila_actual][cont]
        return multiplicarMatriz(matriz1,matriz2,columna,fila,columna_actual,fila_actual+1,suma,result,cont,result2)






#---------------------------------------------------------------------------------------------------------------------
    
def sumaMatrices(matriz1,matriz2):
    if(isinstance(matriz1,list)and isinstance(matriz2,list)):
        if(verificar_aux(matriz1)):
            if(verificar_aux(matriz2)):
                if(tamaño(matriz1))== tamaño(matriz2):
                    return sumaColumnas_aux2(matriz1,0,tamaño(matriz1),0,largo_lista(matriz1[0],0),[],matriz2,[])
                else:
                    return "ERROR,las matrices tiene distinto tamaño"
            else:
                return "ERROR, la matriz2{matriz2} no tiene los parametro solicitados"
        else:
            return "ERROR, la matriz1{matriz1} no tiene los parametro solicitados"
    else:
        return "ERROR, la matriz1 o la matriz2 no son lista."
                
                 
def sumaColumnas_aux2(matriz1,fila_actual,m_filas,columna_actual,n_columnas,suma_columna,matriz2,result):
    if(fila_actual==m_filas):
        return result
    elif(columna_actual==n_columnas):
        return sumaColumnas_aux2(matriz1,fila_actual+1,m_filas,0,n_columnas,[],matriz2,result+[suma_columna])
    else:
        
        suma_columna+=[int(matriz1[fila_actual][columna_actual])+int(matriz2[fila_actual][columna_actual])]
        return sumaColumnas_aux2(matriz1,fila_actual,m_filas,columna_actual+1,n_columnas,suma_columna,matriz2,result)
                   
                
                    


def tamaño(m):
    return tamaño_aux(m,1,0)
def tamaño_aux(m,indice,cont):
    if(largo_lista(m,0))==1:
        return cont+1
    elif(largo_lista(m[0],0))==(largo_lista(m[indice],0)):
        return tamaño_aux(m[1:],indice,cont+1)
    else:
        return False
def largo_lista(lista,cont):
    if(lista==[]):
        return cont
    else:
        return largo_lista(lista[1:],cont+1)
    

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
                
