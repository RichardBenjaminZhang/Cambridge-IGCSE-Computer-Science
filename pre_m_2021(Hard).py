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
while TimeUp!=9 and TimeUp!=11 and TimeUp!=13 and TimeUp!=15:
    TimeUp=int(input("Sorry. The Time is not acceptble."))
for count in range(0,4):
    if TimeUp==Trains_Up_Time[count]:
        IndexUp = count
TimeDown=int(input("What time period ticket you wanna buy? It's 10:00/12:00/14:00/16:00"))
while TimeDown<TimeUp or (TimeDown!=10 and TimeDown!=12 and TimeDown!=14 and TimeDown!=16):
    TimeDown = int(input("Sorry. The Time is not acceptble."))
for count in range(0,4):
    if TimeDown==Trains_Down_Time[count]:
        IndexDown = count
NumTickets=int(input("How many do you wanna buy? The tenth tickets is free."))
while NumTickets > Trains_Up_Tickets[IndexUp] or NumTickets > Trains_Down_Tickets[IndexDown]:
    NumTickets = int(input("Sorry. The Ticket is not acceptble."))
Trains_Up_Tickets[IndexUp]=Trains_Up_Tickets[IndexUp]-NumTickets
Trains_Down_Tickets[IndexDown]=Trains_Down_Tickets[IndexDown]-NumTickets
for count in range(0,4):
    if Trains_Up_Tickets[count]==0:
        Trains_Up_Tickets[count]=str(Trains_Up_Tickets[count])
        Trains_Up_Tickets[count]="Closed"
    if Trains_Down_Tickets[count]==0:
        Trains_Down_Tickets[count]=str(Trains_Down_Tickets[count])
        Trains_Down_Tickets[count]="Closed"
                                     
