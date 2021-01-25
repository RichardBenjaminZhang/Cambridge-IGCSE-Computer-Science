#Task1
Cost=25
Coach_Size=80
Time_Range=8
Total_Passengers=0
Total_Cost=0.0
Coach_1=[0]*TIME_RANGE
Coach_2=[0]*TIME_RANGE
Coach_3=[0]*TIME_RANGE
Coach_4=[0]*TIME_RANGE
Coach_5=[0]*TIME_RANGE
Coach_6=[0]*(TIME_RANGE+2)
available=480

def task_1():
    Total_Up=0.0
    Total_Down=0.0
    print()
    print("*******Tickets Info*******")
    print("Up Time:9:00,11:00,13:00,15:00")
    print("Down Time:10:00,12:00,14:00,16:00")
    print("Avalilable Tickets",avalilable)
#Task2
def task_2():
    total_up=0.0
    total_down=0.0
    coach_1_total=0
    coach_2_total=0
    coach_3_total=0
    coach_4_total=0
    coach_5_total=0
    coach_6_total=0
print(''===========Buying Tickets=============='')
up_time=int(input("Up Time:"))
down_time=int(input("Down Time:"))
tickets=int(input("Passenger Numbers:"))
up_idx=map_time_slot(up_time)
down_idx=map_time_slot(down_time)
global available
if coach_1_total+tickets<=COACH_SIZE:
    coach_1[up_idx]+=tickets
    coach_1=total+tickets
    total_up=COST*tickets
 elif coach_2_total+tickets<=COACH_SIZE:
    coach_2[up_idx]+=tickets
    coach_2=total+tickets
    total_up=COST*tickets
 elif coach_3_total+tickets<=COACH_SIZE:
    coach_3[up_idx]+=tickets
    coach_3=total+tickets
    total_up=COST*tickets
 elif coach_4total+tickets<=COACH_SIZE:
    coach_4[up_idx]+=tickets
    coach_4=total+tickets
    total_up=COST*tickets
 elif coach_5total+tickets<=COACH_SIZE:
    coach_5[up_idx]+=tickets
    coach_5=total+tickets
    total_up=COST*tickets
 elif coach_6total+tickets<=COACH_SIZE:
    coach_6[up_idx]+=tickets
    coach_6=total+tickets
    total_up=COST*tickets
    
