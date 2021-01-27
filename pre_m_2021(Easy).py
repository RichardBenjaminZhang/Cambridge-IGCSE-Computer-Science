#Task1
COST=25
COACH_SIZE=80
TIME_RANGE=8
total_Passengers=0
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
  else:
       print("There is no seat left for you. Closed“）
    if coach_1_total+tickets<=COACH_SIZE:
             coach_1[down_idx]+=tickets
             coach_1=total+tickets
             total_down=COST*tickets
             elif coach_2_total+tickets<=COACH_SIZE:
             coach_2[down_idx]+=tickets
             coach_2=total+tickets
             total_down=COST*tickets
             elif coach_3_total+tickets<=COACH_SIZE:
             coach_3[down_idx]+=tickets
             coach_3=total+tickets
             total_down=COST*tickets
             elif coach_4total+tickets<=COACH_SIZE:
             coach_4[down_idx]+=tickets
             coach_4=total+tickets
             total_dowm=COST*tickets
             elif coach_5total+tickets<=COACH_SIZE:
             coach_5[dowm_idx]+=tickets
             coach_5=total+tickets
             total_down=COST*tickets
             elif coach_6total+tickets<=COACH_SIZE:
             coach_6[down_idx]+=tickets
             coach_6=total+tickets
             total_down=COST*tickets
             elif coach_6[8]+tickets<=COACH_SIZE:
                coach_6[8]+=tickets
             elif coach_6[9]+tickets<=COACH_SIZE:
                coach_6[9]+=tickets
             else:
                  print("There is no seat left for you. You need to wait to the next day to go down the mountain")
             total_cost=total_up+total_down
             print("Total cost for your trip is:",total_cost
                   available-= tickets
def map_time_slot(time):
    if time==9:
         idx=0
   elif time==10:
         idx=1
   elif time==11:
         idx=2
   elif time==12:
         idx=3
   elif time==13:
         idx=4
   elif time==14:
         idx=5
   elif time==15:
         idx=6
   elif time==16:
         idx=7
   return idx
#Task3
def task_3():
    total_tickets=0
    total_money=0.0
    for i in range(6):
 total_tickets+=coach_1[i]+coach_2[i]+coach_3[i]+coach_4[i]+coach_5[i]+coach_6[i]
                 total_money=total_tickets*COST
                 print("total passengers of the day is:",int(total_tickets/2))
                 print("total money of the day is:",total_money)
                   print()
           for i in range(3):
                   task_1()
                   task_2()
                   task_3()
          print(coach_1)
