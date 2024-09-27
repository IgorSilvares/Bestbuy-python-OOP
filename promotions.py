from abc import ABC, abstractmethod

class Promotion(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        total_price = 0
        for i in range(0, quantity):
            if i % 2 == 0:
                total_price += product.price
            else:
                total_price += product.price / 2
        return total_price

    def __str__(self):
        return f"{self.name}"


class ThirdOneFree(Promotion):

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        total_price = 0
        for i in range(quantity):
            if (i+1) % 3 != 0:
                total_price += product.price
        return total_price

    def __str__(self):
        return f"{self.name}"


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return product.price - (product.price * self.percent / 100)

    def __str__(self):
        return f"{self.name}"
