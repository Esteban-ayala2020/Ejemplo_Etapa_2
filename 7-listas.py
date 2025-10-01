# validar si en la siguente lista existen dos números

#contiguos que su suma de el valor de target


lista = [1002,32,12,32,1,2,3,4,6,7,8,9,0,10,2]

target = 12

posiciones = len(lista) - 1
cumple = False

for pos in range(0, posiciones):
    for prx in range(pos + 1, posiciones):
        suma = lista[pos] + lista[prx]
        if (suma == target):
            cumple = True
            print("El valor de la posición: ", pos, "y el valor de posición", prx, "dan el valor del target")


if (not cumple):
    print("ninguno de los valores cumple el target")



# lista.pop(0)

# print(lista)

# conjunto = set(lista)

# print(conjunto)

# lista = list(conjunto)

# print(sorted(lista))
