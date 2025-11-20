class MathUtils:
    PI = 3.14159

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def circle_area(radius):
        return MathUtils.PI * radius ** 2

    @classmethod
    def get_pi(cls):
        return cls.PI


if __name__ == "__main__":
    print(f"20°C = {MathUtils.celsius_to_fahrenheit(20):.1f}°F")
    print(f"68°F = {MathUtils.fahrenheit_to_celsius(68):.1f}°C")
    print(f"Площадь круга с радиусом 5: {MathUtils.circle_area(5):.2f}")
    print(f"Значение PI: {MathUtils.get_pi()}")