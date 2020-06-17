def findName(names,name):
    i=0
    for i in range(5):
        if names[i]=="Susan":
            return True
    
    if i==5:
        return False

names=['Fred','Adam','Bobby','William','Susan']
matched=findName(names,'Susan')
print(matched)
    
