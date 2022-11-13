def multiplicar():
    cantidad = 1
    n=int(input("Cantidad de numeros que va a multiplicar: "))
    for i in range(n):
        valor = int(input("Numero: "))
        cantidad *= valor 

    print("El producto es: ",cantidad)
multiplicar()