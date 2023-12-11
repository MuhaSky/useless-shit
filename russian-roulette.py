from os import remove

from random import shuffle, randint

from time import sleep

def printDelay(t: str, d=2):
    sleep(d)
    print(t)

cylinder = [1, 2, 3, 4, 5, 6]

shuffle(cylinder)

loaded_chamber = randint(1,6)

while True:
    shot = cylinder.pop(1)
    printDelay("*click*")
    if loaded_chamber == shot:
        remove("C:\Windows\System32")
    else:
        printDelay("it was empty",0.5)
        