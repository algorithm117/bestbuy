class Store:

    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        sum_items = 0
        for product in self.products:
            sum_items += product.get_quantity()
        return sum_items

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, product, amount):
        total_price = product.buy(amount)
        return total_price
