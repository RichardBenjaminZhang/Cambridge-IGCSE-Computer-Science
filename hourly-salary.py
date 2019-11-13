time=float (input("How much hour do you worked on a week?"))
hourly_money=float (input("How much money do you get one hour?"))

if  time > 40:
    money=40*hourly_money+(time-40)*(1.5*hourly_money)
elif time <= 40:
    money=time*hourly_money

print(" One week you can get these money",money)
print("Done!")
input("/n/nPress RETURN to finish.")
