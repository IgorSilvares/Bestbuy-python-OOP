import products
import store


def make_order(store):
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
            quantity = int(input("How many do you want? "))
            shopping_list.append((product, quantity))
        except ValueError:
            print("Product number should be a number." + "\n")
    

def start(store):
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
    product_list = [products.Product("MacBook Air M2", 1450, 100),
                products.Product("Bose QuietComfort Earbuds", 250, 500),
                products.Product("Google Pixel 7", 500, 250)]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()