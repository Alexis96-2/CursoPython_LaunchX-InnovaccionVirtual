 # program.py
sum = 1 + 2
# Impresión en pantalla print('Hola desde la consola')
print(sum)
print('Hola desde la consola')
#sum = 1 + 2 da 3
product = sum * 2
print(product)
# Tu turno, prueba el fragmento de código anterior

planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
# Descubrimos su tipo de dato (distancia_a_alfa_centauri)
print(type(distancia_a_alfa_centauri))
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

#OPERADORES
# <left side> <operator> <right side>
left_side = 10
right_side = 5
print(left_side / right_side) # 2

#FECHAS
# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

# CONVERSION DE TIPO DE DATOS
print("Today's date is: " + str(date.today()))

# RECOPILAR INFORMACION
#Entrada del usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)
#Trabajar con numeros
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)
print(int(first_number) + int(second_number))