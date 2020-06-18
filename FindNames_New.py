def findName(names,name):
    i=0
    for i in range(5):
        if names[i]==name:
            return True
    
    if i==5:
        return False

names=['Fred','Adam','Bobby','William','Susan']
name=input("What your name?")
matched=findName(names,name)
print(matched)
