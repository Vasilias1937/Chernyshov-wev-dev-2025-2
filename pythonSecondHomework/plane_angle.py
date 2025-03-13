import math  

class Point:  
    def __init__(self, x, y, z):  
        self.x = x  
        self.y = y  
        self.z = z  

    def __sub__(self, other):  
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)  

    def dot(self, other):  
        return self.x * other.x + self.y * other.y + self.z * other.z  

    def cross(self, other):  
        x = self.y * other.z - self.z * other.y  
        y = self.z * other.x - self.x * other.z  
        z = self.x * other.y - self.y * other.x  
        return Point(x, y, z)  

    def absolute(self):  
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)  

def plane_angle(a, b, c, d):  
    """  
    Вычисляет угол между плоскостями, образованными точками A, B, C и B, C, D в градусах.  
    """  
    ab = b - a  
    bc = c - b  
    cd = d - c  

    x = ab.cross(bc)  
    y = bc.cross(cd)  

    cos_phi = x.dot(y) / (x.absolute() * y.absolute())  
    phi = math.acos(cos_phi)  
    return math.degrees(phi)  

if __name__ == '__main__':  
    a = Point(1, 0, 0)  
    b = Point(0, 1, 0)  
    c = Point(0, 0, 1)  
    d = Point(1, 1, 1)  

    angle = plane_angle(a, b, c, d)  
    print(f"{angle:.2f}")  

    # Пример ввода из условия задачи  
    a = Point(0, 1, 1)  
    b = Point(1, 0, 1)  
    c = Point(1, 1, 0)  
    d = Point(0, 0, 0)  
    angle = plane_angle(a, b, c, d)  
    print(f"{angle:.2f}")  