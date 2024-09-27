from abc import ABC, abstractmethod

class Promotion(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):

    def __init__(self, name):
        """
        Initialize a SecondHalfPrice object with the given name.

        :param name: the name of the promotion
        :type name: str
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Applies the promotion to a given quantity of the product.

        Every second product in the order is sold at half price.

        :param product: the product to apply the promotion to
        :type product: Product
        :param quantity: the quantity of the product to apply the promotion to
        :type quantity: int
        :return: the total cost of the given quantity of the product with the promotion applied
        :rtype: float
        """
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
        """
        Initialize a ThirdOneFree object with the given name.

        :param name: the name of the promotion
        :type name: str
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Applies the promotion to a given quantity of the product.

        Every third product in the order is free.

        :param product: the product to apply the promotion to
        :type product: Product
        :param quantity: the quantity of the product to apply the promotion to
        :type quantity: int
        :return: the total cost of the given quantity of the product with the promotion applied
        :rtype: float
        """
        total_price = 0
        for i in range(quantity):
            if (i+1) % 3 != 0:
                total_price += product.price
        return total_price

    def __str__(self):
        return f"{self.name}"


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        """
        Initialize a PercentDiscount object with the given name and percent discount.

        :param name: the name of the promotion
        :type name: str
        :param percent: the percent discount for the promotion
        :type percent: int
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Applies the promotion to a given quantity of the product.

        The promotion is a percentage discount of the price of the product.

        :param product: the product to apply the promotion to
        :type product: Product
        :param quantity: the quantity of the product to apply the promotion to
        :type quantity: int
        :return: the total cost of the given quantity of the product with the promotion applied
        :rtype: float
        """
        return product.price - (product.price * self.percent / 100)

    def __str__(self):
        return f"{self.name}"

