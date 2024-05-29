from valid_menu import Valid, Menu
from budget_cart import Cart

STORE = {'apple':4, 'orange':6, 'lemon':4, 'pineapple':4, 'banana':6, 'cherry':8, 'blackberry':10}
MIN_BUDGET, MAX_BUDGET = 10, 1000

def set_budget(valid, cart) -> None:
    cart.balance = valid.get_valid_number('Set your Budget from 10 to 1000 USD! ', 10, 1000)

def add_item(valid, cart) -> None:
    item_name = valid.get_valid_string(f'Enter the name of the Item from {STORE} store! ', *STORE)
    item_price = STORE[item_name]
    max_amount = int(cart.balance / item_price)
    amount_to_buy = valid.get_valid_number(f'Enter the quantity of the Item to buy from 0 to {max_amount}! ', 0, max(0, max_amount))
    cart.add_item(item_name, item_price, amount_to_buy)
    print('Item added successfully! ')

def view_cart(cart) -> None: 
    print(cart.to_purchase)

def remove_item(valid, cart) -> None:
    item_names = [item['item_name'] for item in cart.to_purchase]
    item_to_remove = valid.get_valid_string(f'Enter the ame of the Item from {item_names} actual Cart to remove! ', *item_names)
    max_quantity = [item['quantity_to_buy'] for item in cart.to_purchase if item['item_name'] == item_to_remove]
    quantity_to_remove = valid.get_valid_number(f'Enter the quantity (0-{max_quantity[0]}) to remove from the Cart! ', 0, max_quantity[0])
    cart.remove_item(item_to_remove, quantity_to_remove)
    print('Item deleted successfully! ')
    
def view_budget(cart) -> None: 
    print(f'Your current Budget available is {cart.balance} USD. ')

def exit() -> None:
    print('Thank you for choosing us! Good bye! ')
    
def main() -> None:
    valid, menu, cart = Valid(), Menu(), Cart()
    actions = {
        0: lambda: set_budget(valid, cart),
        1: lambda: add_item(valid, cart) if cart.balance else print('Please set up your Budget first! '),
        2: lambda: view_cart(cart),
        3: lambda: remove_item(valid, cart) if cart.to_purchase else print('You cannot remove Item because your Cart is Empty! '),
        4: lambda: view_budget(cart), 
        5: lambda: exit()}
    while True:
        choice = valid.get_valid_number(f'Choose your option from the menu below!\n{menu.options} ', 0, 5)
        if choice == 5: exit(); break
        actions[choice]()
if __name__ == '__main__':  main()