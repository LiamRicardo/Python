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