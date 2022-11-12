# funcion que suma n cantidad de numeros
def suma(n):
    sum = 0
    for i in range(n):
        num = int(input('Ingrese el numero ' + str(i+1) + ': ',))
        sum += num
    return sum