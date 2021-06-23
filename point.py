class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def is_in_rectangle(self, rectangle):
        return rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y

    
    def distance_from_point(self, point) -> float:
        return ((self.x - point.x) ** 2 + (self.y - point.y) **2) ** 0.5 

    