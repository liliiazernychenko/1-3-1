import math


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):

        # перевірка існування трикутника
        if (self.a + self.b <= self.c or
            self.a + self.c <= self.b or
            self.b + self.c <= self.a):
            return 0

        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Circle:

    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2


class Parallelogram:

    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h


class Trapeze:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return 0   # площу не задавали — залишаємо 0


def process_file(filename):

    file = open(filename)

    max_perimeter = 0
    max_area = 0

    max_p_fig = ""
    max_a_fig = ""

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
        a = fig.area()

        if p > max_perimeter:
            max_perimeter = p
            max_p_fig = line.strip()

        if a > max_area:
            max_area = a
            max_a_fig = line.strip()

    file.close()

    print("Файл:", filename)

    print("Фігура з найбільшим периметром:")
    print(max_p_fig)
    print("Периметр =", round(max_perimeter, 2))

    print("Фігура з найбільшою площею:")
    print(max_a_fig)
    print("Площа =", round(max_area, 2))

    print()


process_file("input01.txt")
process_file("input02.txt")
process_file("input03.txt")
