#Task1
Size=3
namesArr=[""]*Size
Marks_1=[0]*Size
Marks_2=[0]*Size
Marks_3=[0]*Size
def setup():
    for i in range(Size):
        Student_Name=input("Student Name?")
        Score_1=int(input("Your Test1 Score?"))
        Score_2=int(input("Your Test2 Score?"))
        Score_3=int(input("Your Test3 Score?"))
        namesArr[i]=Student_Name
        Marks_1[i]=Score_1
        Marks_2[i]=Score_2
        Marks_3[i]=Score_3
setup()
for i in range(Size):
    print(namesArr[i])
    print(Marks_1[i])
    print(Marks_2[i])
    print(Marks_3[i])
#Task2
