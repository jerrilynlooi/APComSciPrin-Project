from cmath import pi, tan
from random import randint
import turtle

win = turtle.Screen()

def move_turtle(coordinates):
    turtle.up()
    turtle.goto(coordinates)
    turtle.down()


def make_dot(coordinates):
    turtle.up()
    turtle.goto(coordinates)
    turtle.down()
    turtle.dot(2)


def draw_corners(size):
    corner_left = (-size/2,-size/2)
    corner_right = (size/2,-size/2)
    corner_top = (0, (size/4) * tan(pi/3))
    corner_list = [corner_left, corner_right, corner_top]
    print(type(corner_list))
    for corner in corner_list:
        make_dot(corner)
    return corner_list


def two_thirds_location(point1, point2):
    x_location = point1[0] + (2 * (point2[0] - point1[0])) / 3
    y_location = point1[1] + (2 * (point2[1] - point1[1])) / 3
    return (x_location, y_location)


def sierpinksi_approx(size, accuracy):
    corner_list = draw_corners(size)
    current_location = corner_list[0]
    for i in range(0, accuracy):
        corner_num = randint(0,2)
        corner = corner_list[corner_num]
        new_location = two_thirds_location(current_location, corner)
        make_dot(new_location)
        current_location = new_location  

def sierpinski(size, depth):
    if depth == 0:
        return None
    else:
        for i in range(0,3):
            sierpinski(size/2,depth-1)
            turtle.forward(size)
            turtle.left(120)

def moved_sierpinski(size, depth):
    move_turtle((-size/2,-size/2))
    sierpinski(size, depth)

'''sierpinksi_approx(100,100)
moved_sierpinski(100,5)'''

win.exitonclick()
