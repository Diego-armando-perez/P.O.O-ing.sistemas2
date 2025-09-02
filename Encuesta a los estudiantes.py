intentos = 1
lista_resultados = []
while intentos != 7:
    print("Estudiante numero " + "[" + str(intentos) + "]")
    nombre = input("¿Cual es su nombre?: ")
    carrera = input("¿Cual es su carrera?: ")
    idea = input("¿Cual es su idea de proyecto?: ")
    w = "Estudiante numero " + "[" + str(intentos) + "] sus respuestas fueron: \n Nombre del estudiante: " + str(nombre) + "\n Carrera del estudiante: " + str(carrera) + "\n Proyecto del estudiante: " + str(idea) + "\n----------------------------"
    lista_resultados.append(w)
    intentos += 1   

print("Gracias por sus participaciones estudiantes, las respuestas de sus participaciones fueron: ")
for i in lista_resultados:
    print (i)