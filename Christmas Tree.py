#Input Turtle database
import turtle
#Set Screen
screen = turtle.Screen()
screen.setup(800,600)
#Get & Identify Pen to draw
circle = turtle.Turtle()

circle.shape('circle')

circle.color('red')

circle.speed('fastest')

#Stop Pen-first time

circle.up()

#Get Pen to draw again

square = turtle.Turtle()

##Get & Identify Pen to draw again

square.shape('square')

square.color('green')

square.speed('fastest')

#Stop Pen-second time

square.up()

#Jump to cordinate

circle.goto(0,280)

#Copy the Shape

circle.stamp()

k = 0

for i in range(1, 17):

    y = 30*i

    for j in range(i-k):

        x = 30*j

        square.goto(x,-y+280)

        square.stamp()

        square.goto(-x,-y+280)

        square.stamp()

    if i % 4 == 0:

        x = 30*(j+1)

        circle.color('red')

        circle.goto(-x,-y+280)

        circle.stamp()

        circle.goto(x,-y+280)

        circle.stamp()

        k += 2

    if i % 4 == 3:

        x = 30*(j+1)

        circle.color('yellow')

        circle.goto(-x,-y+280)

        circle.stamp()

        circle.goto(x,-y+280)

        circle.stamp()

square.color('brown')

for i in range(17,20):

    y = 30*i

    for j in range(3):

        x = 30*j

        square.goto(x,-y+280)

        square.stamp()

        square.goto(-x,-y+280)

        square.stamp()

turtle.exitonclick()
