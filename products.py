class Product:

    def __init__(self, name, price, quantity):

        if name == None or name == "" or price < 0 or quantity < 0:
            raise Exception("Name is empty or price or quantity is negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity <= 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.is_active() or self.get_quantity() < quantity:
            raise Exception("Error while making order! Quantity larger than what exists.")
        self.set_quantity(self.quantity - quantity)
        total_cost = quantity * self.price
        return total_cost


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
