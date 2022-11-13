def MinMax():
    num = int (input ('¿Cuantos numeros  desea introducir?: '))
    Numeros =[]
    for i in range(num):
        Numero=int(input('Ingrese el numero '+ str(i+1) + ': '))
        Numeros.append(Numero)
    Min=Numeros[0]
    for j in range(num):
        if Numeros[j]<Min:
         Min=Numeros[j]
        j=j+1
    Max=Numeros[0]
    for k in range(num):
        if Numeros[k]>Max:
         Max=Numeros[k]
        k=k+1
    print ('Usted introdujo ', num, "numeros")
    print ('El Maximo es: ', Max)
    print ('El Minimo es: ', Min)
MinMax()