#This is Cambridge IGCSE Computer Science 0478/22 2021 Series Pre-Release-Material Model Answer

#Task1
TicketCost=25.00
Trains_Up_Time=[9,11,13,15]
Trains_Up_Tickets=[480,480,480,480]
Trains_Up_Money=[0.0,0.0,0.0,0.0]
Trains_Down_Time=[10,12,14,16]
Trains_Down_Tickets=[480,480,480,640]
Trains_Down_Money=[0.0,0.0,0.0,0.0]
print("Trian Times\t\tTickets Avaiable \tTotal Money for this time")
for count in range(0,4):
    print(Trains_Up_Time[count],"\t\t\t",Trains_Up_Tickets[count],"\t\t\t",Trains_Up_Money[count])
    print(Trains_Down_Time[count],"\t\t\t",Trains_Down_Tickets[count],"\t\t\t",Trains_Down_Money[count])
#Task2
Ticket_Sell="Y"
while Ticket_Sell=="Y":
    TimeUp=int(input("What time period ticket you wanna buy? It's 9:00/11:00/13:00/15:00"))
