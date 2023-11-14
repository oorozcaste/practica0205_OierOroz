def iterativa(n):
    """n sera un numero entero y mediante bucles for esta funcion a 
    la salida nos dara el factorial de ese numero, la variable x en este caso
    nos sive para hacer la multiplicación de todos los numeros anteriores
    pues ser ira actualizando por cada repeticion del bucle for con el valor de la 
    multiplicacion del numero siguiente """
    x = 1
    for i in range(1, n + 1):
         x = x * i
    return x
x = int(input("dime un numero entero: "))
print(iterativa(x))