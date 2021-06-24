"""
    A program that displays a message to the user showing the coordinates of a rectangle.
    The user enters the coordinates of a point to check if they are inside the rectangle.
"""

from guipoint import GuiPoint
from random import randint
from guirectangle import GuiRectangle
import turtle



if __name__ == '__main__':


    rectangle = GuiRectangle(
        GuiPoint(randint(0, 9), randint(0, 9)),
        GuiPoint(randint(10, 19), randint(10, 19))
    )


    print(f"Rectangle Coordinates: ({rectangle.point1.x},{rectangle.point1.y}) and ({rectangle.point2.x},{rectangle.point2.y})")

    user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))

    user_area = float(input("Guess rectangle area: "))

    print(f"Your point was inside the rectangle: {user_point.is_in_rectangle(rectangle)}")

    print(f"Your area was off by: {rectangle.area() - user_area}")

    myturtle = turtle.Turtle()
    rectangle.draw(canvas=myturtle)
    user_point.draw(canvas=myturtle)