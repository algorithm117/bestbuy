class Product():
    def __init__(self, name, price, quantity):

        if name is None or name == "" or price < 0 or quantity < 0:
            raise Exception("Name is empty or price or quantity is negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, type_promotion):
        self.promotion = type_promotion

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
        if self.promotion is not None:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self.promotion.name}"
        else:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if str(type(self)) == "<class 'products.NonStockedProduct'>":
            return self.price
        elif str(type(self)) == "<class 'products.LimitedProduct'>" and quantity > self.maximum:
            raise Exception("Error while making order! Order size cannot be larger than product order limit.")
        elif not self.is_active() or self.get_quantity() < quantity:
            raise Exception("Error while making order! Quantity larger than what exists.")
        self.set_quantity(self.quantity - quantity)
        total_cost = 0
        if self.promotion is not None:
            total_cost = self.promotion.apply_promotion(self, quantity)
        else:
            total_cost = quantity * self.price
        return total_cost


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self):
        if self.promotion is not None:
            return f"{self.name}, Price: {self.price}, Promotion: {self.promotion.name}"
        return f"{self.name}, Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        if self.promotion is not None:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity},  Product Order Limit: {self.maximum}, Promotion: {self.promotion.name}"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Product Order Limit: {self.maximum}"


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
