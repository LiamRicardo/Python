def imprimir_tablero(mesa):
    for fila in mesa:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_ganador(mesa):
    for fila in mesa:
        if fila[0] == fila[1] == fila[2] != " ":
            return True

    for col in range(3):
        if mesa[0][col] == mesa[1][col] == mesa[2][col] != " ":
            return True

    if mesa[0][0] == mesa[1][1] == mesa[2][2] != " ":
        return True
    if mesa[0][2] == mesa[1][1] == mesa[2][0] != " ":
        return True

    return False

def juego_daVelha(mesa, x, y, caracter):
    if mesa[x][y] == " ":
        mesa[x][y] = caracter
        return True
    else:
        return False

def main():
    mesa = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        imprimir_tablero(mesa)
        print(f"Turno del jugador {jugador_actual}")

        try:
            x = int(input("Ingresa la fila (0, 1, 2): "))
            y = int(input("Ingresa la columna (0, 1, 2): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Posición fuera del rango. Inténtalo de nuevo.")
            continue

        if not juego_daVelha(mesa, x, y, jugador_actual):
            print("Posición ocupada. Inténtalo de nuevo.")
            continue

        if verificar_ganador(mesa):
            imprimir_tablero(mesa)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        if all(mesa[i][j] != " " for i in range(3) for j in range(3)):
            imprimir_tablero(mesa)
            print("¡Es un empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

if __name__ == "__main__":
    main()



