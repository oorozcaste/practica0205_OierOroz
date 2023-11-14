def factorial(n):
    """n sera un numero entero que daremos y al la salida
    tendremos el factorial de ese numero"""
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
z = int(input("Dime un numero entero"))
y = factorial(z)
print(y)
    