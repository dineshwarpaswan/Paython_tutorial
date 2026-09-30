class Circle:
    def __init__(self,r):
        self.r = r

    def circleArea(self):
        
        return (22/7) * (self.r*self.r)
    
    def circleParameter(self):
        return (2*22/7) * self.r

area = Circle(7)
print(f"Area of Circle: {area.circleArea()} m^2")
print(f"Parameter of Circle: {area.circleParameter()} m\n")

area = Circle(28)
print(f"Area of Circle: {area.circleArea()} m^2")
print(f"Parameter of Circle: {area.circleParameter()} m")
    
