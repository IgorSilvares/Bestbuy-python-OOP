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
        return (f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    
    def buy(self, quantity):
        """
        Buy the given quantity of the product.

        :param quantity: the quantity of the product to buy
        :type quantity: int
        :return: the total cost of the given quantity of the product
        :rtype: int
        :raises ValueError: if the given quantity is not available in stock
        """
        if self.quantity is None:
            raise ValueError("Quantity should be greater than 0")
        if quantity <= 0:
            raise ValueError("Quantity should be greater than 0")
        if self.quantity < quantity:
            raise ValueError("Quantity not available in stock")
        self.quantity -= quantity
        if self.quantity <= 0:
            self.deactivate()
        return quantity * self.price




