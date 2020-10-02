from math import *
"""
This Functions this only to group data 
"""

def converDataInt(data):
    for i in range(len(data)):
        data[i] = int(data[i])
    return data

        

def varianzaPoblacional(datosPoblacion):
    datosPoblacion = converDataInt(datosPoblacion.split(" "))
    N = len(datosPoblacion)
    mu = promedio(datosPoblacion)
    sumatoria= 0
    for i in datosPoblacion:
        sumatoria += pow((i - mu),2)
    
    print("Varianza Polacional ",sumatoria/N)




def promedio(datosPoblacion):
    promedio=0
    for i in datosPoblacion:
        promedio += float(i)
    return promedio/len(datosPoblacion)


def varianzaMuestral(datosPoblacion):
    datosPoblacion = converDataInt(datosPoblacion.split(" "))
    n = len(datosPoblacion)
    xB = promedio(datosPoblacion)
    sumatoria= 0
    for i in datosPoblacion:
        sumatoria += pow((i - xB),2)
    
    print("Varianza Muestral ", sumatoria/(n-1))

def desviacionEstandarPoblacional(datosPoblacion):
    datosPoblacion = converDataInt(datosPoblacion.split(" "))
    N = len(datosPoblacion)
    mu = promedio(datosPoblacion)
    sumatoria= 0
    for i in datosPoblacion:
        sumatoria += pow((i - mu),2)
    print("Desviacion estandar poblacional ",sqrt(sumatoria/N))



def desviacionEstandarMuestral(datosPoblacion):
    datosPoblacion = converDataInt(datosPoblacion.split(" "))
    n = len(datosPoblacion)
    xB = promedio(datosPoblacion)
    sumatoria= 0
    for i in datosPoblacion:
        sumatoria += pow((i - xB),2)
    
    print("Desviacion estandar muestral ",sqrt(sumatoria/(n-1)))

def convertArray(type,listC):
    for i in range(len(listC)):
        listC[i] = type(listC[i])
    return sorted(listC)

def mediana(listC):
    listC = convertArray(float,listC)
    number = int (len(listC)/2)
    return (listC[number - 1] + listC[(number)])/2 if len(listC)%2 == 0 else listC[number ]

def cuartiles(listC):
    listC = convertArray(float,listC)
    cuartil1 = (0.25 * (len(listC) + 1))
    cuartil2 = (0.5 * (len(listC) + 1))
    cuartil3 = (0.75 * (len(listC) + 1))

    cuartiles = {
        'cuartil1': cuartilesIf(cuartil1,listC),
        'cuartil2': cuartilesIf(cuartil2,listC),
        'cuartil3': cuartilesIf(cuartil3,listC), 

    }
    return cuartiles

def limitesCaja(cuartiles):
    return {'limInf': cuartiles['cuartil1'] - (1.5*(cuartiles['cuartil3']-cuartiles['cuartil1'])),
    'limSup': cuartiles['cuartil3'] + (1.5*(cuartiles['cuartil3']-cuartiles['cuartil1']))}

def cuartilesIf (cuartil,listC):

    if cuartil.is_integer() :
        return listC[int(cuartil-1)]
    else:
        return promedio([listC[int(cuartil-1)],listC[int(cuartil)]])




print(mediana("820.0, 849.3, 899.1, 923.8, 927.7, 943.3, 965.7, 1008.4, 1016.6, 1166.1, 1205.4".split(", ")))
print(mediana("0 0 0 0 0 0 0 1 1 1 1 2 2 2 2 2 2 3 3 33 3 4 4 4 4 5 5 5 6 6 6 6 6 6".split(' ')))
#varianzaPoblacional(data)
#desviacionEstandarPoblacional(data)
cuartilE= cuartiles("706.0, 774.0, 848.6, 885.6, 891.5, 915.0, 948.6, 1012.6, 1024.9, 1130.0, 1249.2, 1308.1".split(", "))
print(cuartilE)
print(limitesCaja(cuartilE))
print(0.75*(12+1))
