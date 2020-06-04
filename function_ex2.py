def get_total():
    number=0
    total=0
    number=int(input("Feed me a number please?"))
    while total <= 20:
        total=total+number
        number=int(input("Feed me a number please?"))
    print(total)
get_total()
