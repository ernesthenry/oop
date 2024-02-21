class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def remove_item(self, index):
        del self.items[index]

    def calculate_total(self):
        total = sum(item.price * quantity for item, quantity in self.items)
        return total

menu = [
    MenuItem("Pizza", 10),
    MenuItem("Burger", 5),
    MenuItem("Ice Cream", 7),
    MenuItem("Chicken Meal", 9),
    MenuItem("Fries", 10),
    MenuItem("Coca-Cola", 6)
]

def display_menu():
    print("Menu:")
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item.name}: ${item.price}")

def main():
    order = Order()
    display_menu()
    while True:
        choice = input("Enter item number to add to order (0 to checkout): ")
        if choice == '0':
            break
        try:
            item_index = int(choice) - 1
            if 0 <= item_index < len(menu):
                quantity = int(input("Enter quantity: "))
                order.add_item(menu[item_index], quantity)
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input.")

    total = order.calculate_total()
    print(f"Total amount: ${total}")

    while True:
        try:
            amount_paid = float(input("Enter amount paid: $"))
            if amount_paid >= total:
                change = amount_paid - total
                print(f"Change: ${change}")
                print("Thank you for your purchase!")
                break
            else:
                print("Insufficient payment.")
        except ValueError:
            print("Invalid input.")

if __name__ == "__main__":
    main()
