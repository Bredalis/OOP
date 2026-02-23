
class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__pi = 3.1415

    def calculate_perimeter(self):
        print(f"Perimeter: {2 * self.__pi * self.__radius}")

    def calculate_area(self):
        print(f"Area: {self.__pi * self.__radius ** 2}")

    def get_pi(self):
        print(f"PI: {self.__pi}")

    def set_radius(self, value):
        try:
            if value <= 0:
                return "Cannot be negative or zero"

            self.__radius = value
            return f"Radius: {self.__radius}"

        except Exception as e:
            print(f"Unexpected error: {e}")


print("Circle properties:\n")

circle = Circle(2.5)

circle.calculate_perimeter()
circle.calculate_area()
circle.get_pi()
print(circle.set_radius(2))
