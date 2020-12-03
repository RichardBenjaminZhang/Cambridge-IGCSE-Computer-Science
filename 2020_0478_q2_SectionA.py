#Task1
Size=3
namesArr=[""]*Size
Marks_1=[0]*Size
Marks_2=[0]*Size
Marks_3=[0]*Size

for i in range(Size):
    Student_Name=input("Student Name?")
    Score_1=int(input("Your Test1 Score?"))
    Score_2=int(input("Your Test2 Score?"))
    Score_3=int(input("Your Test3 Score?"))
    namesArr[i]=Student_Name
    Marks_1[i]=Score_1
    Marks_2[i]=Score_2
    Marks_3[i]=Score_3

for i in range(Size):
    print(namesArr[i])
    print(Marks_1[i])
    print(Marks_2[i])
    print(Marks_3[i])


#Task2
Total_Score=[0]*Size
for i in range(Size):
    Total_Score[i]=Marks_1[i]+Marks_2[i]+Marks_3[i]
    print(Total_Score[i])
    print(namesArr[i])
Class_Total=0
for i in range(Size):
    Class_Total=Class_Total+Total_Score[i]
average=Class_Total/Size
print(average)
#Task3
def select():
    Highest_Score=0
    for i in range(Size):
        if Highest_Score <Total_Score[i]:
            Highest_Score=Total_Score[i]
    #print("The Student name is",namesArr[i])
    print("This student mark is",Highest_Score)
select()
