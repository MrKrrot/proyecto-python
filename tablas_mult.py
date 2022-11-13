def tablas():
    numero = int(input("Introduzca el numero que desea: "))

    for i in range(1,11):
        resultado = i * numero
        print(numero, "X", i, "=", resultado)