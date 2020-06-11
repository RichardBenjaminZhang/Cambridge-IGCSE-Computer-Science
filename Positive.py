import os 
total=0
count=0
while count <= 4:
    number=int(input('You should give me a positive number'))
    if number >= 0:
        total = total + number
        count = count +1
    else:
            print('You should enter a positive number!')
result = total / count
print(' Mean of these number is ', result)
answer=input('Keep do it?')
if answer == 'no':
    os.system('taskkill /f /im py.exe')
else:
    total = 0
    count = 0

    
    
