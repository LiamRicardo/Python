listapro = []
print(listapro)
while True:
    decicion = input("Selecione una acsion(add),(delet),(incertar) o (close): ")

    if decicion == "add":
        numero = int(input("Dijite un numero pues:"))
        listapro.append(int(numero))
        print(listapro)
    elif decicion == "delet":
        numero = int(input("Dijite el numero a cer borrado: "))
        listapro.remove(int(numero))
        print(listapro)
    elif decicion == "incertar":
        indice = int(input("Dijite un numero del indice: "))
        numero = int(input("Dijite un numero a cer insetado: "))
        listapro.insert(int(indice), int(numero))
        print(listapro)
    elif decicion == "close":
        print(listapro)
        break

        