"""
    A program that displays a message to the user showing the coordinates of a rectangle.
    The user enters the coordinates of a point to check if they are inside the rectangle.
"""

from point import Point
from rectangle import Rectangle
from random import randint



if __name__ == '__main__':

    rectangle = Rectangle(
        Point(randint(0, 9), randint(0, 9)),
        Point(randint(10, 19), randint(10, 19))
    )


    print(f"Rectangle Coordinates: ({rectangle.lowleft.x},{rectangle.lowleft.y}) and ({rectangle.upright.x},{rectangle.upright.y})")

    user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))

    user_area = float(input("Guess rectangle area: "))

    print(f"Your point was inside the rectangle: {user_point.is_in_rectangle(rectangle)}")

    print(f"Your area was off by: {rectangle.area() - user_area}")