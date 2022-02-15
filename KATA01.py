#primer programa
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print("La Fecha de Hoy es: " + str(date.today()))
parsec = 11
lightyears = 3.26156 * parsec

print(str(parsec) + " parsec, es " + str(lightyears) + " lightyears")

print("Calculadora parsec a lightyears")
first_number = input("Parsec: ")
second_number = (lightyears)
print(int(first_number) * int(second_number))