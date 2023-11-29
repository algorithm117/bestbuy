import store
import products


def start(store_obj):
    user_choice = None

    while user_choice != 4:

        print("\tStore Menu")
        print("\t__________")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        user_choice = int(input("Please choose a number: "))

        if user_choice == 1:
            print("______")
            all_products = store_obj.get_all_products()
            counter = 1
            for product in all_products:
                print(f"{counter}. {product.show()}")
                counter += 1
            print("______")
        elif user_choice == 2:
            total_items = store_obj.get_total_quantity()
            print(f"Total of {total_items} in store")
        elif user_choice == 3:
            cost = 0
            while True:
                print("______")
                all_products = store_obj.get_all_products()
                counter = 1
                for product in all_products:
                    print(f"{counter}. {product.show()}")
                    counter += 1
                print("______")

                print("When you want to finish order, enter empty text.")
                product_choice = input("Which product # do you want? ")
                amount = input("What amount do you want? ")

                if product_choice == "" or amount == "":
                    break

                price = 0
                product = all_products[int(product_choice) - 1]
                try:
                    price = store_obj.order(product, int(amount))
                except Exception:
                    print("Error while making order! Quantity larger than what exists.")

                cost += price

            print(f"Order made! Total payment: ${cost}")


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    # products.Product(None, -1, -10)
                    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == '__main__':
    main()