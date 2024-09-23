class Product:
    def __init__(self, name, price, quantity):
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




