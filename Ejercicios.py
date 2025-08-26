#Autor: Diego Armando Pérez Solano

# Esto es una prueba para novatos

#1 Ejecute una entrada de texto e imprímala

texto = input("Escriba cualquier cosa aquí: ")
print (texto)

#2 Realizar las tablas de multiplicar con cualquier numero que se introduzca 

numero_a_evaluar = float(input("Ingrese un numero: "))

for i in range (1, 11):
	tabla_multiplicacion = numero_a_evaluar * i
	print(tabla_multiplicacion)

#3 Utilizando una función obtenga el numero factorial de un numero dado

def factorial(x):
	for i in range (1, x):
		x *= i
	return x

numero = int(input("Numero a evaluar factorial: "))

print (factorial(numero))