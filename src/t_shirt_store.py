
class TShirt:
    def __init__(self, size, color, price, brand):
        self.size = size
        self.color = color
        self.price = price
        self.brand = brand
        self.discounted = False

    def apply_discount(self, percentage):
        self.price -= self.price * percentage / 100

        # Set if product is discounted
        if percentage < 100:
            self.discounted = True

    def display_information(self):
        info = (
            f"\nT-shirt description:\n"
            f"Brand: {self.brand}\n"
            f"Price: ${self.price:.2f}\n"
            f"Color: {self.color}\n"
            f"Size: {self.size}\n"
        )

        print(info)

        if not self.discounted:
            return "\nThis product is not discounted"
        return "\nThis product is discounted"


t_shirts = [
    TShirt("M", "Black", 100, "Gucci"),
    TShirt("M", "Red", 30, "Adidas"),
]

for shirt in t_shirts:
    print(shirt.display_information())
    shirt.apply_discount(50)
    print(shirt.display_information())
