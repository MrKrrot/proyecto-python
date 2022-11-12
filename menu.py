import os
import time
import pyfiglet

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

def menu():
    seconds = 2
    for i in range(0, seconds):
        print(' ')
        os.system("clear")
        print(P+'=============================================='+B)
        print(R + pyfiglet.figlet_format("Proyecto"))
        print(B + pyfiglet.figlet_format("FINAL 2"))
        print(P+'=============================================='+B)
        print(O+'Skip in...' + str(seconds-i)+G)
        time.sleep(1)