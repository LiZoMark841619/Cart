from valid_menu import Valid, Menu
from budget_cart import Cart

OPTIONS = {'apple', 'orange', 'lemon', 'pineapple', 'banana', 'cherry', 'blackberry'}
MIN_BUDGET, MAX_BUDGET = 10, 1000
MIN_ITEM_PRICE, MAX_ITEM_PRICE = 1, 100

def set_budget(valid, cart):
    cart.budget = valid.get_valid_number('Enter your budget from 10 to 1000 USD! ', 10, 1000)

def add_item(valid, cart):
    if cart.budget:
        item_name = valid.get_valid_string(f'Enter the name of the items from {OPTIONS} options! ', *OPTIONS)
        item_price = valid.get_valid_number(f'Enter the price of the item from {MIN_ITEM_PRICE} to {MAX_ITEM_PRICE} USD! ', MIN_ITEM_PRICE, MAX_ITEM_PRICE)
        max_amount = int(cart.budget / item_price)
        amount_to_buy = valid.get_valid_number(f'Enter the amount of the item from 0 to {max_amount}! ', 0, max(0, max_amount))
        cart.add_item(item_name, item_price, amount_to_buy)
        print('Item added successfully! ')
    else:
        print('Please set up your budget first! ')

def view_cart(cart): 
    print(cart.to_purchase)

def remove_item(valid, cart):
    cart.remove_item(valid.get_valid_string(f'Enter the name of the items from {OPTIONS} options! ', *OPTIONS))

def view_budget(cart): 
    print(f'Your current budget available is {cart.budget} USD. ')

def exit():
    print('Thank you for choosing us! Good bye! ')
    
def main():
    valid, menu, cart = Valid(), Menu(), Cart()
    actions = {
        0: lambda: set_budget(valid, cart),
        1: lambda: add_item(valid, cart),
        2: lambda: view_cart(cart),
        3: lambda: remove_item(valid, cart),
        4: lambda: view_budget(cart),
        5: lambda: exit()
    }
    while True:
        choice = valid.get_valid_number(f'Choose your option from the menu below!\n{menu.options} ', 0, 5)
        actions[choice]()
        
if __name__ == '__main__': main()