import turtle

def draw_triangle(brad):
 
    line_num = 0
    while line_num < 3:
      brad.forward(150)
      brad.right(120)
 #     brad.backward(150)
 #     brad.left(90)
      line_num += 1

 #   brad.right(10)
#    brad.forward(150)
 #    brad.forward(150)

#draw_square()
"""
square_num = 30
angle = 360/square_num
intital_angle = 0
while intital_angle < 360:
    draw_square()
    intital_angle += 30
"""
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("white")
    brad.speed(200)
    triangle_num = 10
    brad = turtle.Turtle()
    for i in range (triangle_num):
       draw_triangle(brad)
       brad.right(36)
 
draw_art()
