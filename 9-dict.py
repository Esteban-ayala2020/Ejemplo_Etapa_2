# en función del nombre del mes quiero que me diga
# a que numero corresponde
# por ej. Agosto --> 8

mes = {"enero":"1",
       "febrero":"2",
       "marzo": "3",
       "abril":"4",
       "mayo":"5",
       "junio":"6",
       "julio":"7",
       "agosto":"8",
       "septiembre":"9",
       "octubre":"10",
       "noviembre":"11",
       "diciembre":"12"}

# print(mes)
usuario= input("Ingrese en Nombre del Mes: ").lower()
# for valor in mes.items():
if usuario in mes:
    print(f"El numero del mes es: {mes[usuario]}")
else:
    print("El mes ingresado no es valido")
