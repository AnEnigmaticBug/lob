class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def magnitude(self):
        return self.x ** 2 + self.y ** 2
    
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vec(self.x * other, self.y * other)
    
    def __truediv__(self, other):
        return Vec(self.x / other, self.y / other)
    
    def __radd__(self, other):
        return self + other
    
    def __rsub__(self, other):
        return self - other
    
    def __rmul__(self, other):
        return self * other
    