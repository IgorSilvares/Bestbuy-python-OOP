import products 
import store
from products import LimitedProduct


def make_order(store):
    """
    Present a menu of products and quantities to the user, and
    return an order (a list of (product, quantity) tuples) to the caller.

    :param store: the store to order from
    :type store: Store
    :return: the order
    :rtype: list of (Product, int)
    """
    shopping_list = []
    products = store.get_all_products()
    while True:
        print("----------")
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product.show()}")
        print("----------")
        print("When you want to finish order, enter empty text.")
        product_number = input("Which product # do you want? ")
        if product_number == "":
            print(store.order(shopping_list))
            break
        try:
            product_number = int(product_number)
            if product_number < 1 or product_number > len(products):
                raise ValueError
                continue
            product = products[product_number - 1]
            if isinstance(product, LimitedProduct):
                max_quantity = product.maximum
            else:
                max_quantity = product.get_quantity()
            while True:
                quantity = int(input("How many do you want? "))
                if quantity <= 0 or quantity > max_quantity:
                    print("Invalid quantity. Please try again or enter empty text to cancelR." + "\n")
                else:
                    break
            shopping_list.append((product, quantity))
        except ValueError:
            print("Product number should be a number." + "\n")
    

def start(store):
    """
    Present a menu of options to the user, and respond to the user's
    choices by calling other functions.

    :param store: the store to interact with
    :type store: Store
    """
    while True:
        print("Store Menu\n----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        user_choise = input("Please choose a number: ")
        print()

        if user_choise == "1":
            for i, product in enumerate(store.get_all_products(), start=1):
               print(f"{i}. {product.show()}")
            print()
        if user_choise == "2":
            print(f"Total of {store.get_total_quantity()} items in store")
            print("------")
        if user_choise == "3":
            make_order(store)
        if user_choise == "4":
            break


def main():
    # setup initial stock of inventory
    """
    The main entry point for the program.

    Sets up an initial store with some products, and then enters a loop
    where it repeatedly asks the user for input.
    """
# setup initial stock of inventory
    product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()