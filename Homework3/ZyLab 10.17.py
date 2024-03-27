# Dominic Jason 2203959

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self, item_name, item_quantity, item_price):
        total = item_price * item_quantity
        print(f'{item_name} {item_quantity:.0f} @ ${item_price:.0f} = ${total:.0f}')


if __name__ == "__main__":
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    print("Item 1")
    item1.item_name = input("Enter the item name:")
    item1.item_price = float(input("\nEnter the item price:"))
    item1.item_quantity = int(input("\nEnter the item quantity:\n"))

    print("\nItem 2")
    item2.item_name = input("Enter the item name:")
    item2.item_price = float(input("\nEnter the item price:"))
    item2.item_quantity = int(input("\nEnter the item quantity:\n"))

    print("\nTOTAL COST")
    item1.print_item_cost(item1.item_name, item1.item_quantity, item1.item_price)
    item2.print_item_cost(item2.item_name, item2.item_quantity, item2.item_price)
    print()
    total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
    print(f'Total: ${total_cost:.0f}')
