#TPI 2 Simulacion, UTN FRRE Junio de 2020
#Alejandro Fabian Nadal
#Docente: Ing Carlos Vecchi

import generadores

def corridaSemana(info = False):
    horasSemana= 168
    horasClase = 34

    semana=[]
    dia=[]
    #Estructura de matriz
    #HorasPreparacion | HorasInconveniente | HorasSuenio | HorasPersonales
    horasPorActividadTotal=[0,0,0,0]
    for i in range(0,7):
        dia.append(generadores.generarHorasPreparacion())
        horasPorActividadTotal[0] += dia[0]
        dia.append(generadores.generarHorasInconveniente())
        horasPorActividadTotal[1] += dia[1]
        #Como las horas de suenio varian dependiendo del dia, ponemos un condicional
        
        if i < 5:
            dia.append(generadores.generarHorasSuenioSemana())
        else:
            dia.append(generadores.generarHorasSuenioFinSemana())
        horasPorActividadTotal[2] += dia[2]
        dia.append(generadores.generarHorasPersonales())
        horasPorActividadTotal[3] += dia[3]
        #Agregamos el dia a la semana
        semana.append(dia)
        #reiniciamos el dia
        dia = []
    if info:
        for dia in semana:
            print(dia)
    if info:
        print("Acumulado Horas")
        print(horasPorActividadTotal)
    #Ahora se generan la cantidad de tareas para la semana
    tareaSemanales = generadores.generarCantidadTareas()
    if info:
        print("La cantidad de tareas es ",tareaSemanales)
    
    #Ahora, calculamos la cantidad de horas que tomara cada tarea
    horasPorTarea=[]
    for i in range(0,tareaSemanales):
        horasPorTarea.append(generadores.generarHorasTarea())
    
    horasNoTareas= sum(horasPorActividadTotal)
    if info:
        print("Horas para cada tarea" +str(horasPorTarea))
    horasTareas= sum(horasPorTarea)
    if info:
        print("Horas totales en la semana" + str(horasSemana))
        print("Horas utilizadas:" + str(horasNoTareas))
        print("Horas a utilizar en tareas: "+str(horasTareas))
        print("Horas Libres" +str(horasSemana-horasNoTareas-horasClase))

    return ((horasSemana - horasNoTareas -horasClase) > horasTareas) 
    
    

     

    


corridaSemana()