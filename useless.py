from random import randint
from os import remove

if randint(0, 6) == 1:
    remove("useless.py")