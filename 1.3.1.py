import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimeter(self):
        return 2 * (self.a + self.b)

class Circle:
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return 2 * math.pi * self.r

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def perimeter(self):
        return 2 * (self.a + self.b)

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimeter(self):
        return self.a + self.b + self.c + self.d

def process_file(filename):
    file = open(filename)
    max_perimeter = 0
    max_figure = ""
    for line in file:
        parts = line.split()
        name = parts[0]
        if name == "Triangle":
            fig = Triangle(float(parts[1]), float(parts[2]), float(parts[3]))
        elif name == "Rectangle":
            fig = Rectangle(float(parts[1]), float(parts[2]))
        elif name == "Circle":
            fig = Circle(float(parts[1]))
        elif name == "Parallelogram":
            fig = Parallelogram(float(parts[1]), float(parts[2]), float(parts[3]))
        elif name == "Trapeze":
            fig = Trapeze(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]))
        p = fig.perimeter()
        if p > max_perimeter:
            max_perimeter = p
            max_figure = line.strip()

    file.close()

    print("Файл:", filename)
    print("Фігура з найбільшим периметром:")
    print(max_figure)
    print("Периметр =", max_perimeter)
    print()


process_file("input01.txt")
process_file("input02.txt")
process_file("input03.txt")
