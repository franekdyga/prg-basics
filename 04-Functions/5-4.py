import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length

def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)
    pen.hideturtle()
    window.mainloop()

def draw_triangle(length):
    pen.right(60)
    pen.forward(1/3*(length))
    pen.right(120)
    pen.forward(1/3*(length))
    pen.right(120)
    pen.forward(1/3*(length))   
    pen.hideturtle()
    window.mainloop()

# a = int(input(f'input length: '))
# draw_square(a)

draw_triangle(200)