from time import *

def type(str):
    for lettr in str:
        print(lettr, end ='')
        sleep(0.015)
    print('')

def typeTime(str, time):
    for lettr in str:
        print(lettr, end ='')
        sleep(float(time))
