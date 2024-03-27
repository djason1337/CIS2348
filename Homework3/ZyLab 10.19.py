# Dominic Jason 2203959

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity:.0f} @ ${self.item_price:.0f} = ${total:.0f}')

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')


class ShoppingCart:
    def __init__(self, customer_name='none', current_date="January 1, 2016", cart_items=0):
        cart_items = []
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print('Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase):
        is_item_found = 0
        quantity = input('Enter the new quantity:\n')
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                is_item_found = 1

                ItemToPurchase = item
                ItemToPurchase.item_quantity = quantity
                return
        if is_item_found == 0:
            print('Item not found in cart. Nothing modified.\n')

    def get_num_items_in_cart(self):
        quantity = 0
        for item in self.cart_items:
            quantity += int(item.item_quantity)
        return quantity

    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += int(item.item_price) * int(item.item_quantity)
        return cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print('OUTPUT SHOPPING CART')
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print('Number of Items: 0\n')
            print('SHOPPING CART IS EMPTY\n')
            print('Total: $0\n')
            print_menu()
        else:
            print('OUTPUT SHOPPING CART')
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            num_items = self.get_num_items_in_cart()
            print(f'Number of Items: {num_items}\n')
            total = self.get_cost_of_cart()
            for item in self.cart_items:
                print(f'{item.item_name} {item.item_quantity} @ ${item.item_price} = ${int(item.item_price) * int(item.item_quantity)}')
            print(f'\nTotal: ${total}\n')
            print_menu()


    def print_descriptions(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}\n')
        print('Item Descriptions')
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_description}')


if __name__ == "__main__":
    customer_name = input('Enter customer\'s name:\n')
    current_date = input('Enter today\'s date:\n')
    print(f'\nCustomer name: {customer_name}')
    print(f'Today\'s date: {current_date}\n')

    def print_menu():
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')


    print_menu()
    cart = ShoppingCart(customer_name, current_date)

    while True:

        option = input('\nChoose an option:\n')
        possible_options = ['a', 'r', 'c', 'i', 'o', 'q']

        if option not in possible_options:
            option = input('Choose an option:')
            continue
        if option == 'a':
            print('ADD ITEM TO CART')
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)
            print()
            print_menu()
        elif option == 'r':
            print('REMOVE ITEM FROM CART')
            item = input('Enter name of item to remove:\n')
            cart.remove_item(item)
            print()
            print_menu()
        elif option == 'c':
            print('CHANGE ITEM QUANTITY')
            item = input('Enter the item name:\n')
            item = ItemToPurchase(item)
            cart.modify_item(item)
            print_menu()
        elif option == 'i':
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            cart.print_descriptions()
            print()
            print_menu()
        elif option == 'o':
            cart.print_total()
        elif option == 'q':
            break
