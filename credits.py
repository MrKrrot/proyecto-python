import pyfiglet
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

def credits():
    print(P+'======================================================')
    print(G + pyfiglet.figlet_format("Integrantes")+B)
    print(P+'======================================================'+B)
    print('  - Camacho Trejo Aurora Cristal')
    print('  - Curiel Román Mario Iván')
    print('  - Sánchez Olguín Rafael')
    print('  - Villareal De Leija Angela Elizabeth')