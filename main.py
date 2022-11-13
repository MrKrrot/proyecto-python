import os
import inquirer
import pyfiglet
import time
from credits import credits
from menu import menu
from suma import suma
from mul import multiplicar
from tablas_mult import tablas
from factorial import factorial
from cubo_cuadrado import CubCua
from promedio import promedio
from division import division

G  = '\033[32m'
W  = '\033[0m'

def main():

    menu()
    os.system("clear")
    
    while True:
        print(G+pyfiglet.figlet_format("Menu"))
        questions = [
            inquirer.List('operation',
            message="¿Qué operación desea realizar?",
            choices=['Suma', 'Producto', 'División', 'Factorial', 'Tablas Multiplicar', 'Cuadrado y Cubo', 'Promedio', 'Máximo y mínimo', 'Salir'],
            ),
        ]
        answer = inquirer.prompt(questions).get('operation')
        
        os.system("clear")
        print('Elegiste: '+ G + answer + W)
    
        if(answer == 'Suma'):
            n = int(input('¿Cuántos numeros desea sumar? '))
            print(suma(n))

        elif(answer == 'Producto'):
            print('Aquí se hará el producto')

        elif(answer == 'División'):
            division()

        elif(answer == 'Factorial'):
            num = int(input('¿Qué número desea calcular su factorial? '))
            print(factorial(num))

        elif(answer == 'Tablas Multiplicar'):
            print('Aquí se harán las tablas de multiplicar')

        elif(answer == 'Cuadrado y Cubo'):
            CubCua()

        elif(answer == 'Promedio'):
            promedio()

        elif(answer == 'Máximo y mínimo'):
            print('Aquí se hará el máximo y mínimo')
        else:
            break

        time.sleep(2)
        os.system("clear")
    
    credits()
if __name__ == '__main__':
    main()