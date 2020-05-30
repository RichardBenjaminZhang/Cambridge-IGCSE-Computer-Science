num=0
total=0
present = 0
for i in range(20):
    present= int(input("Type value here:"))
    if present >0:
        total += present
        num+=1
print(total/num)
