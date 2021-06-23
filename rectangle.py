class Rectangle:
    
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    
    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)