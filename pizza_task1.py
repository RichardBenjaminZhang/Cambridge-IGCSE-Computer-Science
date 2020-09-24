SIZE=10
pizza_code=['']*SIZE
pizza_price=[2.00,5.00,5.55,7.00,7.50,9.00,11.00,12.00,14.50,4.50]
pizza_menu=['French fries','1/4 pound burger','1/4 pound cheeseburger','1/2 pound burger','1/2 pound cheeseburger','Medium pizza','Medium pizza with extra toppings','Large pizza','Large pizza with extra toppings','Garlic bread']

def setup_code(p_code):
    for i in range(SIZE):
        p_code[i]='L_id'+str(i)
    print(p_code)


setup_code(pizza_code)
