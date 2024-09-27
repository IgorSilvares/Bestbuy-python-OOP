import promotions

class Product:
    def __init__(self, name, price, quantity):
        """
        Initialize a Product object with the given name, price, and quantity.

        :param name: the name of the product
        :type name: str
        :param price: the price of the product
        :type price: int
        :param quantity: the quantity of the product
        :type quantity: int
        """
        if name is None:
            raise ValueError("Name should not be empty")
        if name == "":
            raise ValueError("Name should not be empty")
        if price <= 0:
            raise ValueError("Price should be greater than 0")
        if quantity <= 0:
            raise ValueError("Quantity should be greater than 0")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self):
        """
        Return the quantity of the product.

        :return: the quantity of the product
        :rtype: int
        """
        return self.quantity

    
    def set_quantity(self, quantity):
        """
        Set the quantity of the product to the given value.

        :param quantity: the quantity of the product
        :type quantity: int
        """
        self.quantity = quantity

        if self.quantity <= 0:
            self.deactivate()
        if self.quantity > 0:
            self.activate()

    def is_active(self):
        """
        Return whether the product is currently active.

        :return: whether the product is active
        :rtype: bool
        """
        return self.active
    

    def activate(self):
        """
        Activate the product.

        :return: None
        :rtype: None
        """
        
        self.active = True
    

    def deactivate(self):
        """
        Deactivate the product.

        :return: None
        :rtype: None
        """
        self.active = False


    def show(self):
        """
        Return a string describing the product.

        :return: a string describing the product
        :rtype: str
        """
        quantity = self.get_quantity()
        promotion = self.get_promotion()
        return (f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {promotion}")

    
    def buy(self, quantity):
        """
        Buy the given quantity of the product.

        :param quantity: the quantity of the product to buy
        :type quantity: int
        :return: the total cost of the given quantity of the product
        :rtype: int
        :raises ValueError: if the given quantity is not available in stock
        """
        if self.quantity is None or quantity <= 0:
            raise ValueError("Quantity should be greater than 0")
        if self.quantity < quantity:
            raise ValueError("Quantity not available in stock")
        self.quantity -= quantity
        if self.quantity <= 0:
            self.deactivate()

        if self.promotion != None:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return quantity * self.price


    def set_promotion(self, promotion):
        """
        Set the promotion for the product.

        :param promotion: the promotion to set
        :type promotion: Promotion
        """
        self.promotion = promotion

        
    def get_promotion(self):
        """
        Return the promotion for the product.

        :return: the promotion for the product
        :rtype: Promotion
        """
        return self.promotion


class NonStockedProduct(Product):
    def __init__(self, name, price):
        """
        Initialize a NonStockedProduct object with the given name and price.

        :param name: the name of the product
        :type name: str
        :param price: the price of the product
        :type price: int
        """
        super().__init__(name, price, float("inf"))

    def get_quantity(self):
        """
        Return the quantity of the product.

        :return: the quantity of the product
        :rtype: int
        """
        
        return float("inf")

    def show(self):
        """
        Return a string describing the product.

        :return: a string describing the product
        :rtype: str
        """
        promotion = self.get_promotion()
        return (f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {promotion}")

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        """
        Initialize a LimitedProduct object with the given name, price, quantity, and maximum.

        :param name: the name of the product
        :type name: str
        :param price: the price of the product
        :type price: int
        :param quantity: the quantity of the product
        :type quantity: int
        :param maximum: the maximum amount that can be ordered in one order
        :type maximum: int
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """
        Buy the given quantity of the product.

        :param quantity: the quantity of the product to buy
        :type quantity: int
        :return: the total cost of the given quantity of the product
        :rtype: int
        :raises ValueError: if the given quantity is not available in stock
        :raises ValueError: if the given quantity exceeds the maximum allowed
        """
        if quantity > self.maximum:
            raise ValueError("Quantity exceeds maximum allowed")
        return super().buy(quantity)


    def show(self):
        """
        Return a string describing the product.

        :return: a string describing the product
        :rtype: str
        """
        promotion = self.get_promotion()
        return (f"{self.name}, Price: ${self.price}, limited to {self.maximum} per order! Promotion: {promotion}")



