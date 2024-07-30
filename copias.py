#while True:
#    numero = int(input("Porfabor coloque un nuemnro aqui:   "))
#    if numero == -1:
#        break
#    while numero > 0:
#     print(numero)
#     numero -= 1



def media_aritmetica(a, b, c):
    media = (a + b + c) / 3
    print("La media aritmética es:", media)

media_aritmetica(4, 8, 12)



def A(texto, vezes):
    print(texto * vezes)


A("Hola", 3)


def c(tamano):
    fila = "#" * tamano
    contador = 0
    while contador < tamano:
        print(fila)
        contador += 1
c(5)


def mesaXanderz()
    











def comprimentar(nome):
    print("Ola," nome)

def cumprimento_variaz_vezes(nome, vezes):
    while vezes > 0:
        comprimentar(nome)
        vezes -= 1

cumprimento_variaz_vezes("Emily", 3)





numeros = []
numeros.apped(5)
numeros.apped(10)
numeros.apped(3)

print(numeros)







milista = [7, 4, 3, 2]

print(milista[0])









lista = []
while True:
    numeros = input("Coloque números aquí (pero si digita -1 se cerrará): ")
    
    if numeros == '-1':
        break
    lista.append(int(numeros))

print("Lista final:", lista)







listapro = []
print(listapro)
while True:
    decicion = input("Selecione una acsion(add) o (delet)")

    if decicion == "add":
        numero = input(int("Dijite un numero pues:"))
        listapro.append(int(numero))
        print(listapro)
        decicion = input("Selecione una acsion(add) o (delet)")
    if decicion == "delet":
        numero = input(int("Dijite el numero a cer borrado:"))
        listapro.remove(int(numero))
        print(listapro)
        decicion = input("Selecione una acsion(add) o (delet)")
    else:
        print("FATAL ERROR")
        break
print(Listapro)












m = [3, 4, 5, 5]
m.sort()#esto ase que se enumer de menor para el mayor
print(m)




mx = [3, 4, 5, 5]
m = sorted(mx)#esto ase que se enumer de menor para el mayor
print(mx)
print(m)










for i in range(5, 4, 6,):
    print(i)
         
N = int(input("Digite um inteiro positivo: "))
while N <= 0:
    print("Erro: o numeo deve ser positivo. ")
else:
    for i in range(-N, N + 1):
        print(i)
 
def lista_estrelas(lista):
    for numero in lista:
        print("*" * numero)
 
def anagramas(str1, str2):
    return sorted(str1) == sorted(str2)
print(anagramas("listen", "silent"))








milista = [[5,6,7],[9,8],[4,6,1,8,9]]
print(milista)
print(milista[1])
print(milista[1][0])





pesosas = [["Betty",10,1.45],["Abuela",72,1.41],["LASL",4,12.4]]
for pesoa in pesosas:
    nome = pesoa[0]
    idade = pesoa[1]
    altura = pesoa[2]