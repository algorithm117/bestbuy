from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, promotion, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        price = product.price * quantity
        price_after_promotion = price - price * (self.percent / 100)
        return price_after_promotion


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity < 2:
            return product.price
        else:
            price = (quantity // 2) * product.price + (quantity // 2) * product.price * 0.5
            return price


class ThirdOneFree(Promotion):

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity < 2:
            return product.price
        count = 0
        price = 0
        while count < quantity:
            count = count + 1
            if count % 3 == 0:
                continue
            price = price + product.price
        return price
