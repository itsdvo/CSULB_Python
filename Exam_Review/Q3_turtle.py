import turtle

import random

random.seed(2023)

COLORS = ["beige", "coral", "gold", "blue", "green"]

# Set up the screen
screen = turtle.Screen()

# Create turtle
t = turtle.Turtle()
t.speed(100)  # Set to the fastest speed

# Function to draw the X and Y axes
def draw_axes():
    t.penup()
    t.goto(-500, 0)
    t.pendown()
    t.forward(1000)  # Draw the X-axis
    t.penup()
    t.goto(0, -500)
    t.pendown()
    t.left(90)
    t.forward(1000)  # Draw the Y-axis
    t.right(90)  # Reset orientation to initial
    t.penup()

# Function to draw circle
def draw_circles():
    radius = 50
    for _ in range(30):
        t.penup()
        t.goto(0, -radius)  # Setting the starting point so circle centers at (0, 0)
        t.pendown()

        # Choose a random color
        t.color(COLORS[random.randint(0, len(COLORS)-1)])

        t.circle(radius)
        radius += 10  # Increase the radius

# Function to draw an enclosing square around the outermost circle
def draw_enclosing_square(radius):
    # Calculate half the side of the square
    half_side = radius
    
    # Move turtle to bottom-left corner of the square
    t.penup()
    t.goto(-half_side, -half_side)
    t.pendown()
    
    t.color("red")
    
    # Draw the square
    for _ in range(4):
        t.forward(radius * 2)
        t.left(90)

# Draw the axes
draw_axes()

# Draw circles
draw_circles()

# After drawing circles
final_radius = 50 + 10 * 29
draw_enclosing_square(final_radius)

# Keep the window open
screen.mainloop()

