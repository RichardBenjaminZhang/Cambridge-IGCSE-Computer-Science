total=0
count=0
num=0
while count <= 5:
    num=int(input("Please enter a number"))
    if num > 0:
               total = total+num
               count=count+1
    else:
        print("You need enter a POSSITIVE NUMBER")
