import random
Days = 31
def setup():
    mid_night = [0.0] * Days
    for i in range(len(mid_night)):
        mid_night[i]=round(random.uniform(15,50),1)
    return mid_night
 

def display(temp):
    for i in range(len(temp)):
        print(temp[i])


def average(temp):
    avg = 0
    total=0
    for i in range(len(temp)):
        total=temp[i]+total
    avg=total/Days
   

    return avg


def highest(temp):
    highest = 0

def lowest(temp):
    lowest=60.00

    return highest


#tester
month=setup()
print(month)
a=average(month)
print(a)
