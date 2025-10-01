# Determinar si el usuario, el cual
# ingresa por pantalla su anio de nacimiento
# es mayor o menor de edad

anio_usuario = int(input("Ingrese su año de nacimiento:"))
anio_actual = 2025

edad = anio_actual - anio_usuario

mayor_edad = 18

if (edad >= mayor_edad):
    print("Usted es Mayor de Edad")

else:
    print("Usted No es MAYOR de EDAD")