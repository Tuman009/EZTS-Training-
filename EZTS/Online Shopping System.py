class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
    
    def __str__(self):
        return f"{self.name} - Price: ${self.price} - Stock: {self.stock_quantity}"

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity

    def remove_product(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id] -= quantity
            if self.items[product.product_id] <= 0:
                del self.items[product.product_id]

    def view_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            total = 0
            print("Shopping Cart:")
            for product_id, quantity in self.items.items():
                product = product_catalog[product_id]
                subtotal = product.price * quantity
                print(f"{product.name} - Quantity: {quantity} - Subtotal: ${subtotal}")
                total += subtotal
            print(f"Total: ${total}")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.shopping_cart = ShoppingCart()
        self.order_history = []

    def login(self, username, password):
        return self.username == username and self.password == password

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity):
        self.shopping_cart.remove_product(product, quantity)

    def view_cart(self):
        self.shopping_cart.view_cart()

    def checkout(self):
        order = {**self.shopping_cart.items}
        self.order_history.append(order)
        for product_id, quantity in self.shopping_cart.items.items():
            product_catalog[product_id].stock_quantity -= quantity
        self.shopping_cart.items.clear()

    def view_order_history(self):
        if not self.order_history:
            print("No order history.")
        else:
            print("Order History:")
            for index, order in enumerate(self.order_history, start=1):
                print(f"Order {index}:")
                for product_id, quantity in order.items():
                    product = product_catalog[product_id]
                    print(f"{product.name} - Quantity: {quantity}")


# Example usage:

# Sample product catalog
product_catalog = {
    1: Product(1, "Laptop", 1000, 10),
    2: Product(2, "Mouse", 20, 50),
    3: Product(3, "Keyboard", 50, 30)
}

# Creating users
users = {
    "alice": User("alice", "password"),
    "bob": User("bob", "password123")
}

# User login (authentication)
def authenticate(username, password):
    if username in users:
        user = users[username]
        if user.login(username, password):
            return user
    return None

# Test scenario
print("Welcome to our online shopping system.")

# Alice adds products to her cart
alice = authenticate("alice", "password")
if alice:
    alice.add_to_cart(product_catalog[1], 2)
    alice.add_to_cart(product_catalog[2], 1)
    alice.view_cart()

# Bob adds products to his cart
bob = authenticate("bob", "password123")
if bob:
    bob.add_to_cart(product_catalog[2], 3)
    bob.view_cart()

# Alice removes a product from her cart
if alice:
    alice.remove_from_cart(product_catalog[1], 1)
    alice.view_cart()

# Alice checks out her cart
if alice:
    alice.checkout()
    alice.view_order_history()

# Bob checks out his cart
if bob:
    bob.checkout()
    bob.view_order_history()
