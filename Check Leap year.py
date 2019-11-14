year = input("Can you enter a year?：")
year = int(year)
result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if result:
    s = "Yes it is a "
else:
    s = "Not a"
print("{0}{1} Leap year".format(year, s))
# End nicely by waiting for the user to press the return key.
input("\n\nPress RETURN to finish.")
