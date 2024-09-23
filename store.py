class Store:
    def __init__(self, product_list):
        self.product_list = []
        for product in product_list:
            self.add_product(product)


    def add_product(self, product):
        self.product_list.append(product)


    def remove_product(self, product):
        self.product_list.remove(product)


    def get_all_products(self):
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    
    def get_total_quantity(self):
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity


    def order(self, shopping_list):
        total_price = 0
        for product in shopping_list:
            try:
                total_price += product[0].buy(product[1])
            except ValueError as e:
                print(f"Error: {e}")
        return (f"Order cost: {total_price} dollars.")

    