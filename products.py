class Product():
    def __init__(self, name, price, quantity):
        """
        Initialize a product.
        
        :param name(str): The name of the product.
        :param price(float): The price of the product.
        :param quantity(int): The quantity of the product.
        """
        if name is None:
            raise ValueError("Name should not be empty")
        if price < 0:
            raise ValueError("Price should not be less than 0")
        if quantity < 0:
            raise ValueError("Quantity should not be less than 0")
        
        self.name = name
        self.price = prices
        self.quantity = quantity
        self.active = True

    def get_quantity(self, quantity):
        return self.quantity

    
    def set_quantity(self, quantity):
        self.quantity = quantity


    def is_active(self):
        return self.active
    

    def activate(self):
        self.active = True
    

    def deactivate(self):
        self.active = False


    def show(self):
        return (f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    
    def buy(self, quantity):
        if self.quantity is None:
            raise ValueError("Quantity should be greater than 0")
        if quantity <= 0:
            raise ValueError("Quantity should be greater than 0")
        if self.quantity < quantity:
            raise ValueError("Quantity not available in stock")
        self.quantity -= quantity
        return quantity * self.price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())


if __name__ == "__main__":
    main()
