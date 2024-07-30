def tablero_ajedrez(tamano):
    fila = 0
    while fila < tamano:
        columna = 0
        linea = ""
        while columna < tamano:
            if (fila + columna) % 2 == 0:
                linea += "Abuela"
            else:
                linea += "0"
            columna += 1
        print(linea)
        fila += 1

# Ejemplo de uso
tablero_ajedrez(4)



def c(tamano,lineas):
    fila = "Abuela" * tamano
    contador = 0
    while contador < tamano:
        print(fila)
        contador += 1
c(5)


def crear_piramide(tamano, nivel=1):
    if nivel > tamano:
        return
    espacios = ' ' * (tamano - nivel)
    caracteres = '#' * (2 * nivel - 1)
    print(espacios + caracteres + espacios)
    crear_piramide(tamano, nivel + 1)

tamaño_piramide = int(input("Introduce el tamaño de la pirámide: "))
crear_piramide(tamaño_piramide)








def numeros_pares():
    pares = []
    for i in range(0, 39, 2):
        pares.append(i)
    print(pares)

numeros_pares()




def lista_suma(lista1, lista2):
    resultado = []

    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            suma = lista1[i] + lista2[i]
            resultado.append(suma)
        print(resultado)
    else:
        print("Las listas no tienen la misma longitud.")

lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

lista_suma(lista1, lista2)


sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [0, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [0, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 3, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

for item in sudoku:
    for itens in item:
        if itens ==0:
            print('_',end="")
        else:
            print(itens, end="")
    print("")


