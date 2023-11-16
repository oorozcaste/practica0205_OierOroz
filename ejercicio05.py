def erroa(y):
    berbi = []
    for i in y:
        x = i**2
        berbi.append(x)
    return berbi

    
lista = []
while True:
    numeros = int(input("dime numeros hasta que quieras,cuando termines escribe 00: "))
    if numeros == 00:
        break
    else:
        lista.append(numeros)
print(erroa(lista))