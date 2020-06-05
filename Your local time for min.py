import random
from datetime import datetime

size=50000
def setup():
    lst=[]
    for i in range(size):
        num=random.randrange(0,size)
        lst.append(num)
    return lst

def swap(i,j,lst):
    m=lst[i]
    lst[i]=lst[j]
    lst[j]=m

  
def bubblesort(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                swap(i,j,lst)
                

lst=setup()
start_time=datetime.now().strftime("%M%S")
print(datetime.now())
bubblesort(lst)
end_time=datetime.now().strftime("%M%S")
print('the time used is:',int(end_time)-int(start_time),'second')

def insertsort(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        j=i-1
        while j>=0 and lst[j]>key:
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=key

start_time=datetime.now().strftime("%M%S")
insertsort(lst)
end_time=datetime.now().strftime("%M%S")
print('the time used is:',int(end_time)-int(start_time),'second')


    
