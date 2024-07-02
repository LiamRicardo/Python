



#ACTIVIDADE 42
tentativas = 0
while True:
   codigo = input("Porfavor didite seu PIN:")
   tentativas += 1
   if codigo == "4321":
      sueso = True
      break
   if tentativas == 3:
     sueso = False
   print("Incorrecto volver")

if sueso:
   print("PIN Correcto Inserido")
else:
   print("Muitas tentativas")