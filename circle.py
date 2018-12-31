'''Define a class named Circle which can be constructed by a radius. The Circle class has two methods
 area(self) - returns the area of a circle
 perimeter(self) - return the perimeter of the circle'''

class Circle():
    def __init__(self,radius):
        self.radius=radius

   

    def calculate_area(self):
        
        a=3.14*(self.radius**2)
        print("area is: ",a)

    def calculate_peri(self):
        
        peri=2*3.14*self.radius
        print("peri is: ",peri)

obj=Circle(5)
obj.calculate_area()
obj.calculate_peri()
