"""
nombre:
entrada:
salida:
restricciones:
"""


def sumaFila(fila):
    if(fila==[]):
        return 0
    else:
        return fila[0]+sumarFilas(fila[1:])

def sumarFilas(m):
    return sumarFilas_aux(m,[])
def sumaFilas_aux(matriz,result):
    if(matriz==[]):
        return result
    else:
        result+=[sumarfila([0])]
        return sumarFilas_Aux(matriz[1:],result)

"""
nombre:
entrada:
salida:
restricciones:
"""
def sumarfila2(fila):
    if(fila ==[]):
        return 0
    else:
        return fila[0]+sumarFilas2(fila(fila[1:])
def sumaFilas2(m):
    return sumarFilas_aux2(m,0,len(m),[])
def sumarFilas_aux2(matriz,fila_actual,total_filas,result):
    if(fila_actual==total_filas):
        return result
    else:
        result+=[sumarFila2(matriz[fila_actual])]
        return sumarFilas_aux2(matriz,fila_actual+1,total_filas,result)
    

"""
"""
#sum filas 3


def sumarFilas3(m):
    return sumarFilas_aux3(m[1:],m[0],0,[])
def sumarFilas_aux3(matriz,fila_actual,suma_fila,result):
    if(matriz==[])and fila_actual[1:]==[]:
        return resultado+[suma_fila+fila_actual[0]]
    elif(fila_actual==[]):
        return sumarFilas_aux3(matriz[1:],matriz[0],0,resultado+[suma_fila])
    else:
        return sumarFilas_aux3(matriz,fila_actual[1:],suma_fila+fila_actual[0],result)


"""
"""
#sumar colunas
def obtenerColumna(m,indice):
    if(m==[]):
        return []
    else:
        return [m[0][indice]]+obtenerColumna(m[1:],indice)

def sumaColumnas(m):
    if m!=[]:
        return sumaColumnas_aux(m,0,len(m[0]),[])
    
def sumaColumnas_aux(m,columna_Actual,n_columnas,result):
    if(columna_actual==n_columnas):
        return result
    else:
        suma_columna=sumarFila(obtenerColumna(m,columna_actual))
        return sumaColumnas_aux(m,columna_Actual+1,n_columnas,result+[suma_columna])
"""
"""
#sumar columnas 2

def sumaColumnas2(m):
    if(m!=[]):
        return sumaColumnas_aux2(m,0,len(m),len(m[0]),0,[])
def sumaColumnas_aux2(m,fila_actual,m_filas,columna_actual,n_columnas,suma_columna,result):
    if(columna_actual==n_columnas):
        return result
    elif(fila_actual==m_filas):
        return sumaColumnas_aux2(m,0,m_filas,columna_actual+1,n_columnas,0,result+[suma_columna])
    else:
        suma_columna+=m[fila_actual][columna_actual]
        return sumaColumnas_aux2(m,fila_actual,m_filas+1,columna_actual,n_columnas,suma_columna,result)
