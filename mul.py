def multiplicar():
    cantidad = 1
    n=int(input("¿Cuántos numeros desea multiplicar? "))
    for i in range(n):
        valor = int(input("Ingrese el numero " + str(i+1) + ": "))
        cantidad *= valor 

    print("El producto es: ",cantidad)