class GroceryStore:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name]['quantity'] >= quantity:
                self.inventory[item_name]['quantity'] -= quantity
                if self.inventory[item_name]['quantity'] == 0:
                    del self.inventory[item_name]
            else:
                print(f"Not enough {item_name} in stock.")
        else:
            print(f"{item_name} not found in inventory.")

    def check_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("\nAvailable Products:")
            print("------------------")
            for item, details in self.inventory.items():
                print(f"{item}: {details['quantity']} kg @ Rs. {details['price']} per kg")
            print("------------------")


def display_products(store):
    store.check_inventory()


def purchase_item(store):
    order_items = {}
    customer_order = input("\nEnter your order (e.g., Apples:2, Bananas:3): ")
    try:
        for item in customer_order.split(','):
            name, quantity = item.strip().split(':')
            order_items[name.strip()] = int(quantity.strip())
    except ValueError:
        print("Invalid input format.")
        return

    generate_receipt(store, order_items)

    # Deduct purchased items
    for item, quantity in order_items.items():
        store.remove_item(item, quantity)


def generate_receipt(store, items):
    total_cost = 0
    print("\nCustomer Receipt")
    print("------------------")
    for item, quantity in items.items():
        if item in store.inventory and store.inventory[item]['quantity'] >= quantity:
            price = store.inventory[item]['price']
            cost = price * quantity
            total_cost += cost
            print(f"{item}: {quantity} kg @ Rs. {price}/kg = Rs. {cost}")
        else:
            print(f"{item}: Insufficient stock or not found.")
    print("------------------")
    print(f"Total Amount Due: Rs. {total_cost}")


if __name__ == "__main__":
    store = GroceryStore()
    # Preload inventory
    store.add_item("Apples", 50, 300)
    store.add_item("Bananas", 30, 200)
    store.add_item("Oranges", 20, 250)
    store.add_item("Grapes", 15, 400)

    print("Welcome to the Grocery Store!")

    while True:
        print("\n1. View Products\n2. Purchase Items\n3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            display_products(store)
        elif choice == "2":
            purchase_item(store)
        elif choice == "3":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")
