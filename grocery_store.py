class GroceryStore:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        """Add or update an item in the inventory."""
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}

    def remove_item(self, item_name, quantity):
        """Remove a quantity of an item from the inventory."""
        if item_name not in self.inventory:
            print(f"{item_name} not found in inventory.")
            return

        available = self.inventory[item_name]['quantity']
        if quantity > available:
            print(f"Not enough {item_name} in stock. Available: {available}")
            return

        self.inventory[item_name]['quantity'] -= quantity
        print(f"Removed {quantity} of {item_name}. Remaining: {self.inventory[item_name]['quantity']}")

        if self.inventory[item_name]['quantity'] == 0:
            del self.inventory[item_name]

    def check_inventory(self):
        """Display the current inventory."""
        if not self.inventory:
            print("Inventory is empty.")
            return

        print("\n--- Current Inventory ---")
        for item, details in self.inventory.items():
            print(f"{item}: {details['quantity']} kg at Rs. {details['price']}/kg")

    def generate_receipt(self, items):
        """Generate a receipt for customer items and update stock."""
        total_cost = 0
        print("\n--- Customer Receipt ---")
        for item, quantity in items.items():
            if item in self.inventory and self.inventory[item]['quantity'] >= quantity:
                unit_price = self.inventory[item]['price']
                cost = unit_price * quantity
                total_cost += cost
                print(f"{item}: {quantity} kg x Rs. {unit_price} = Rs. {cost}")
                self.remove_item(item, quantity)
            else:
                print(f"⚠️  Insufficient stock or unavailable item: {item}")
        print(f"----------------------------\nTotal Cost: Rs. {total_cost}\nThank you for shopping!\n")


if __name__ == "__main__":
    store = GroceryStore()

    # Add initial inventory
    store.add_item("Apples", 50, 300)
    store.add_item("Bananas", 30, 200)
    store.add_item("Oranges", 20, 250)
    store.add_item("Grapes", 15, 400)

    store.check_inventory()

    # Take customer input
    try:
        customer_order = input("\nEnter your order (e.g., Apples:2, Bananas:3): ")
        order_items = {}

        for item in customer_order.split(','):
            name, quantity = item.split(':')
            name = name.strip().capitalize()
            quantity = int(quantity.strip())
            if quantity <= 0:
                print(f"Invalid quantity for {name}. Skipping.")
                continue
            order_items[name] = quantity

        store.generate_receipt(order_items)
        store.check_inventory()

    except Exception as e:
        print(f"❌ Error processing order: {e}")
