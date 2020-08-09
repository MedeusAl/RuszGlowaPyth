import time
import random
from datetime import datetime
from os import getcwd

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

right_this_minute = datetime.today().minute

A = "tekst IF"
B = "tekst ELSE"
if right_this_minute in odds:
    print("Ta minuta wydaje się być dość nieparzysta")
else:
    print("Minuta parzysta")

print(A)
print(getcwd())

for num in range (random.randint(1, 10)):
    if datetime.today().second in odds:
        print("nieparzyste")
    else:
        print("parzyste")
    time.sleep(random.randint(0,3))

for num in range (5):
    nowa_minuta = random.randint(1, 60)
    if nowa_minuta in odds:
        print("Liczba " + str(nowa_minuta) + " jest nieparzysta")
    else:
        print("Liczba " + str(nowa_minuta) + " jest parzysta")
    time.sleep(2)

for jakas_liczba in range (10, 0, -1):
    print(jakas_liczba)
    if jakas_liczba != 1:
        nowa_liczba = jakas_liczba - 1
        print("Nastepna liczba to: ", nowa_liczba)
