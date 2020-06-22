#TPI 2 Simulacion, UTN FRRE Junio de 2020
#Alejandro Fabian Nadal
#Docente: Ing Carlos Vecchi

import generadores

def corridaSemana():
    horasSemana= 168
    horasClase = 34

    semana=[]
    dia=[]
    for i in range(0,7):
        dia.append(generadores.generarHorasPreparacion())
        dia.append(generadores.generarHorasInconveniente())
        
        #Como las horas de suenio varian dependiendo del dia, ponemos un condicional
        
        if i < 5:
            dia.append(generadores.generarHorasSuenioSemana())
        else:
            dia.append(generadores.generarHorasSuenioFinSemana())

        dia.append(generadores.generarHorasPersonales()) 
        #Agregamos el dia a la semana
        semana.append(dia)
        #reiniciamos el dia
        dia = []
    
    for dia in semana:
        print(dia)

corridaSemana()