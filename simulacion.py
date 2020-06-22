#TPI 2 Simulacion, UTN FRRE Junio de 2020
#Alejandro Fabian Nadal
#Docente: Ing Carlos Vecchi

import corrida as c

registroSemanas = []
for i in range(0,300):
    registroSemanas.append(c.corridaSemana(True))

quiebres = registroSemanas.count(False)
print(registroSemanas)
print("Tras simular 300 semanas, la probabilidad de que al alumno no le alcance el quiebre es de "+str(quiebres*100/300)+"%")