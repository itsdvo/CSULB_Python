# target turtle

import math
import random
import turtle

# constants use all uppercase

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPEED = 3
TARGET_LOWER_LEFT_X = 100
TARGET_LOWER_LEFT_Y = 100
TARGET_WIDTH = 100
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270
SEED = 20230925

def initialize():
    
    random.seed(SEED)

    my_turtle = turtle.Turtle()
    my_turtle.speed(SPEED)

    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
    return my_turtle

def draw_target(t):
    t.hideturtle()
    t.penup()
    t.goto(TARGET_LOWER_LEFT_X,TARGET_LOWER_LEFT_Y)
    t.pendown()
    t.showturtle()

    t.setheading(EAST)
    t.forward(TARGET_WIDTH)

    t.setheading(NORTH)
    t.forward(TARGET_WIDTH)
    
    t.setheading(WEST)
    t.forward(TARGET_WIDTH)

    t.setheading(SOUTH)
    t.forward(TARGET_WIDTH)

    t.penup()
    t.home()

def launch_test(t):
    angle = random.randint(0,90)
    t.setheading(angle)

    distance = random.randint(0,300)
    t.pendown()
    t.forward(distance)

    (x,y) = t.xcor(), t.ycor()

    is_x_in = TARGET_LOWER_LEFT_X <= x <= TARGET_LOWER_LEFT_X + TARGET_WIDTH
    is_y_in = TARGET_LOWER_LEFT_Y <= y <= TARGET_LOWER_LEFT_Y + TARGET_WIDTH
    is_hit = is_x_in and is_y_in

    if is_hit:
        print('bingo')
    else:
        print('miss')

def main():
    # initilize graphics
    t = initialize()
    # draw the square
    draw_target(t)
    # launch the turtle test
    launch_test(t)


    # keeps graphic on last line of your code
    t.screen.mainloop()

main()
