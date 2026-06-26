class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)
        
    def get_diagonal(self):
        return ((self.width ** 2) +(self.height ** 2))**0.5
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_picture(self):
        picture =""
        if self.width>50 or self.height >50:
            return f'Too big for picture.'
        else:
            for line in range(0,self.height):
                picture += "*"*self.width + f'\n'
            return picture
    def get_amount_inside(self,inside_shape):
        if self.width >= inside_shape.width and self.height >= inside_shape.height:
            return (self.width // inside_shape.width) * (self.height//inside_shape.height)
        else:
            return 0

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side # or self.set_side(side)
        self.height = side 

    def set_height(self, side):
        self.width = side # or self.set_side(side)
        self.height = side

    def __str__(self):
        return f'Square(side={self.height})'

sample_rectangle = Rectangle(10, 3)
sample_square = Square(4)

print(sample_rectangle)
print(sample_rectangle.get_picture())

print(sample_square)
print(sample_square.get_picture())

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
