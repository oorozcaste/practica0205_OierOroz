def borobila(radio):
    """en esta funcion le daremos un numero que sera el radio y la función
    nos dara el area"""
    import math
    x = math.pi *radio**2
    return x
def cilindro(altura, radio):
    """en esta funcion nosotros le daremos el numero de la altura
    y haciendo uso de la anterior funcion (borobila) nos dara el volumen
    del cilindro"""
    area = borobila(radio)
    volumen = area * altura
    return volumen
c = float(input("Dime el radio del circulo:"))
print("el area de tu circulo sera:",borobila(c))
v = float(input("dime la altura de tu cilindro: "))
print("el volumen del cilindro con la altura y el circulo con el area dad por ti es ",cilindro(v,c))
