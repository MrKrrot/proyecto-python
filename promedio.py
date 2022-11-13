def promedio():
    print ('Inserte -1 cuando desee dejar de teclear numeros')
    list = []
    suma = 0
    while True:
        num = int(input('Inserte un numero: '))
        if num == -1:
            break
        else:
            list.append(num)
            suma +=num
    print ('El promedio es:',suma/len(list))