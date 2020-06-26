#TPI 2 Simulacion, UTN FRRE Junio de 2020
#Alejandro Fabian Nadal
#Docente: Ing Carlos Vecchi
#Pruebas de numeros pseudoaleatorios
import statistics as stat
import random as ran
import scipy.stats
import math
from time import sleep
import numpy as np


ran.seed(14)

print("Generando 1000 Numeros pseudoaleatorios")

numeros=[]
for i in range(0,10000):
    numeros.append(ran.random())
i=0
while i < 9996:
    print(str(numeros[i])+" "+str(numeros[i+1])+" "+str(numeros[i+2])+" "+str(numeros[i+3])+" "+str(numeros[i+4]))
    i+=4

print("Ejecutando prueba de medias...")
media =round(stat.mean(numeros),4)
print("El alfa utilizado es de 0.05")
alfa=0.95
print("La media es "+str(media))

infMedia=round(0.5-scipy.stats.norm.ppf(alfa)*(1/math.sqrt(12*10000)),4)

supMedia=round(0.5+scipy.stats.norm.ppf(alfa)*(1/math.sqrt(12*10000)),4)

print("Limite inferior "+str(infMedia))
print("Limite superior "+str(supMedia))
if media > infMedia and media < supMedia:
    print("Como la media se encuentra entre los extremos, no podemos rechazar este conjunto de valores")
    continuar=True
else:
    print("Como la media se encuentra fuera de los extremos, se rechazan los valores pseudoaleatorios")
    exit()
sleep(1)
print("----------------------------------------")
print("Iniciando prueba de varianza")

varianza = round(stat.variance(numeros),8)
print("La varianza es de "+str(varianza))
chival1=scipy.stats.chi2.ppf(0.025,len(numeros)-1)
chival2=scipy.stats.chi2.ppf(0.975,len(numeros)-1)
print(chival1)
varInf=chival1/(12*len(numeros)-1)
varInf=round(varInf,4)
varSup=chival2/(12*len(numeros)-1)
varSup=round(varSup,4)

print("Limite Inferior "+str(varInf))
print("Limite Superior "+str(varSup))

if varianza > varInf and varianza < varSup:
    print("Debido a que la varianza se encuentra entre los limites, no se puede rechazar este conjunto de numeros pseudoaleatorios")
else:
    print("La varianza no se encuentra entre los limites, se rechaza el conjunto de numeros pseudoaleatorios")
    exit()
sleep(1)

print("-----------------------------------------")
print("Realizando pruebas de uniformidad")

numIntervalos=math.ceil(math.sqrt(len(numeros)))
print("Numero de intervalos "+str(numIntervalos))


arreglo= np.array(numeros)
hist,bins= np.histogram(arreglo,np.arange(start=0,stop=1,step=0.01))
print("Existen 100 intervalos, divididos equitativamentre entre 0 y 1.La cantidad de ocurrencias por intervalo se imprime debajo")
print(hist)

print("El valor esperado por cada intervalo es 100")
esperada=np.full((99),100)

powerArray= np.full(99,2)
resul=np.power((esperada-hist),powerArray)/esperada 
valorObtenido = np.sum(resul)

valorControl=scipy.stats.chi2.ppf(alfa+(1-alfa)/2,99)

print("Valor Obtenido "+str(valorObtenido))
print("Valor de control "+str(valorControl))

if valorObtenido < valorControl:
    print("Como el valor de control es mayor al obtenido, no se puede rechazar este conjunto de valores")
else:
    print("Este conjunto de valores se rechaza porque el valor de control es menor al obtenido")
print("--------------------------------------------")
sleep(2)
print("Iniciando pruebas de independencia, corridas arriba y abajo")

i=0
c=0
corridas=[]
for i in range(0,9999):
    if numeros[i] < numeros[i+1]:
        corridas.append(1)
    else:
        corridas.append(0)

for i in range(0, len(corridas)-1):
    if corridas[i] != corridas[i+1]:
        c+=1
print("El conjunto S es: ")
print(corridas)
#c=len(corridas)
print("Cantidad de corridas "+str(c))
mediaC=(2*len(numeros)-1)/3
print("Media "+str(mediaC))
varianzaC=(16*len(numeros)-29)/90
print("Varianza "+str(varianzaC))
estadistico=abs(c-mediaC)/math.sqrt(varianzaC)
print("Estadistico Z0 "+str(estadistico))

valorControlIndep=scipy.stats.norm.ppf(0.975)
print("Valor de control "+str(valorControlIndep))

if valorControlIndep >estadistico:
    print("El conjunto de valores no puede ser rechazado y puede ser usado para pruebas estadisticas")
else:
    print("El conjunto de valores es rechazado y no puede ser usado para pruebas estadisticas")

