import requests
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")

print(RED+"██╗███╗░░██╗███████╗░█████╗░░░░░░░░█████╗░███████╗██╗░░░░░██╗░░░░░")
print("██║████╗░██║██╔════╝██╔══██╗░░░░░░██╔══██╗██╔════╝██║░░░░░██║░░░░░")
print("██║██╔██╗██║█████╗░░██║░░██║█████╗██║░░╚═╝█████╗░░██║░░░░░██║░░░░░")
print("██║██║╚████║██╔══╝░░██║░░██║╚════╝██║░░██╗██╔══╝░░██║░░░░░██║░░░░░")
print("██║██║░╚███║██║░░░░░╚█████╔╝░░░░░░╚█████╔╝███████╗███████╗███████╗")
print("╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░░░░░░░░╚════╝░╚══════╝╚══════╝╚══════╝ \n ")
print("\033[33m--------------------------------------")
print(YELLOW+"Autor    : ZE4N")
print("--------------------------------------")
print("INSTAGRAM: ze4n.sh")
print("--------------------------------------")
print("TIK TOK  : zean.py")
print("-------------------------------------- \n")
print(GREEN+"escribe el numero de telefono junto\ncon el prefijo, ejemplo: +526621745707\n")

api_key = '4786cb2a49b771695a8438449b2c6412'

number = int(input(GREEN+"Numero de telefono: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))
