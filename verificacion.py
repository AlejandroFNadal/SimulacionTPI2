import generadores

print("Generacion de valores de prueba")

print("Generar Cantidad de Tareas")
for i in range(0,100):
    print(generadores.generarCantidadTareas())

print("100 valores de la funcion GenerarHorasTarea")
for i in range(0,100):
    print(generadores.generarHorasTarea())

print("100 valores de la funcion GenerarHorasSuenioSemana")
for i in range(0,100):
    print(generadores.generarHorasSuenioSemana())

print("100 valores de la funcion GenerarHorasSuenioFinSemana")
for i in range(0,100):
    print(generadores.generarHorasSuenioFinSemana())

print("100 valores de la funcion generarHorasPreparacion")
for i in range(0,100):
    print(generadores.generarHorasPreparacion())

print("100 valores de la funcion generarHorasPersonales")
for i in range(0,100):
    print(generadores.generarHorasPersonales())


for i in range(0,100):
    print(generadores.generarHorasInconveniente())