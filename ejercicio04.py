
def batezbestekoa(zem):
    gehiketa = sum(zem)
    zenbat = len(zem)
    bataz = gehiketa/zenbat
    return bataz    
zenbakiak=[]
while True:
    x = int(input("dime un numero,cuando ya hayas terminado escribe 00: " ))
    if x == 00:
        break
    else:
        zenbakiak.append(x)
resultado =batezbestekoa(zenbakiak)
print(resultado)