#TPI 2 Simulacion, UTN FRRE Junio de 2020
#Alejandro Fabian Nadal
#Docente: Ing Carlos Vecchi

import random as ran
#Generar horas de suenio. Siguen una distribucion uniforme

def generarHorasSuenioSemana():
    return round(ran.uniform(6.0779,7.9881),2)

def generarHorasSuenioFinSemana():
    return round(ran.uniform(6.8209,9.9891),2)

def generarHorasPersonales():
    return round(ran.normalvariate(1.74,0.44227),2)

def generarHorasPreparacion():
    return round(ran.uniform(0.97396, 2.506),2)

def generarHorasInconveniente():
    return round(ran.uniform(0.02831,3.9783),2)

def generarHorasTarea():
    return round(ran.normalvariate(5.645,2.1594),2)

def generarCantidadTareas():
    return round(ran.choices([1,2,3,4,5,6,7],weights=[5,11,18,16,13,21,16],k=1)[0],2)


