def caixa_hastag(nome):
    print("##########", nome)

def cumprimento_variaz_vezes(nome, vezes):
    while vezes > 0:
        caixa_hastag(nome)
        vezes -= 1

cumprimento_variaz_vezes("",10)



