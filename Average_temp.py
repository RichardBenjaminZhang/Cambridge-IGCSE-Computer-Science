import random


def setup():
    DAYS = 31
    mid_night = [0.0] * DAYS
    for i in range(len(mid_night)):
        mid_night[i]=round(random.uniform(15,50),1)
        return mid_night


def display(temp):
    for i in range(len(temp)):
        print(temp[i])


def average(temp):
    avg = 0
   mid_daytotal=0; mid_nighttotal=0
    return avg


def highest(temp):
    highest = 0

def lowest(temp):
    lowest=100.00

    return highest
