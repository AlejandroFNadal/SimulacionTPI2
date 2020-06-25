import statistics as stat
import math 

#TPI 2 Simulacion, UTN FRRE Junio de 2020
#Alejandro Fabian Nadal
#Docente: Ing Carlos Vecchi

import corrida as c

print("Bienvenido. Este programa hace una simulacion de el comportamiento de un estudiante")

print("Desea obtener los valores internos de cada corrida?")
print("Presione 1 y luego Enter para ver los valores internos de cada corrida")
print("Presione 2 y luego Enter para ver solo los resultados finales")
 

valueMostrar=int(input())

mostrar= False

if valueMostrar == 1:
    mostrar = True

registroSemanas = []
for i in range(0,300):
    registroSemanas.append(c.corridaSemana(mostrar))

quiebres = registroSemanas.count(False)

print("Quiebres")
for i in range(0,300):
    if registroSemanas[i]:
        val="No"
    else:
        val="Si"
    print("Dia: "+str(i)+" Resultado "+val)
print("----------------------------------")
print("Tras simular 300 semanas, la probabilidad de que al alumno no le alcancen las horas es de "+str(round((quiebres*100/300),4))+"% , habiendo ocurrido "+str(quiebres)+" quiebres")

#Para poder calcular intervalos, paso los valores booleanos a numeros
datosfinales=[]
for i in registroSemanas:
    if i:
        datosfinales.append(1)
        #print(1)
    else:
        datosfinales.append(0)
        #print(0)

media = round(stat.mean(datosfinales),4)
varianza = round(stat.variance(datosfinales),4)

alfa=0.05
limiteInferior = round(media - varianza/math.sqrt(300*alfa/2),4)
limiteSuperior = round(media + varianza/math.sqrt(300*alfa/2),4)

print("Con una media de "+ str(media)+" en un intervalo de confianza con un limite inferior  "+str(limiteInferior)+" y superior de "+str(limiteSuperior))

print("La varianza de los resultados fue "+ str(varianza))


print("La media se encuentra dentro del intervalo de confianza")


