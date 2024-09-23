class Store:
    def __init__(self, product_list):
        """
        Initialize a Store object with the given list of products.

        :param product_list: the list of products to put in the store
        :type product_list: list of Product
        """
        self.product_list = []
        for product in product_list:
            self.add_product(product)


    def add_product(self, product):
        """
        Add a product to the store's inventory.

        :param product: the product to add
        :type product: Product
        """
        
        self.product_list.append(product)


    def remove_product(self, product):
        """
        Remove a product from the store's inventory.

        :param product: the product to remove
        :type product: Product
        """
        self.product_list.remove(product)


    def get_all_products(self):
        """
        Return a list of all products in the store that are currently active.

        :return: the list of active products
        :rtype: list of Product
        """
        
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    
    def get_total_quantity(self):
        """
        Return the total quantity of all products in the store.

        :return: the total quantity of all products in the store
        :rtype: int
        """
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity


    def order(self, shopping_list):
        """
        Given a list of (Product, int) tuples representing the items ordered, computes the total cost of the order.

        :param shopping_list: the list of items in the order
        :type shopping_list: list of (Product, int)
        :return: a string describing the total cost of the order
        :rtype: str
        """
        total_price = 0
        for product in shopping_list:
            try:
                total_price += product[0].buy(product[1])
            except ValueError as e:
                print(f"Error: {e}")
        return (f"Order cost: {total_price} dollars.")

    