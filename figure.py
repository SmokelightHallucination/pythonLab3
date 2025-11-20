import math


class Shape:
    def area(self):
        raise NotImplementedError("Метод area должен быть реализован в дочернем классе")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter должен быть реализован в дочернем классе")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Прямоугольник: {self.width}x{self.height}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Круг: радиус {self.radius}"


if __name__ == "__main__":
    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    print(rectangle)
    print(f"Площадь: {rectangle.area()}")
    print(f"Периметр: {rectangle.perimeter()}")

    print(f"\n{circle}")
    print(f"Площадь: {circle.area():.2f}")
    print(f"Периметр: {circle.perimeter():.2f}")