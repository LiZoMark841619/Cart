from valid_menu import Valid, Menu
from budget_cart import Cart

def main():
    valid, menu, cart = Valid(), Menu(), Cart()
    while True:
        options = ['apple', 'orange', 'lemon', 'pineapple', 'banana', 'cherry', 'blackberry']
        choice = valid.get_valid_number(f'Choose your option from the menu below!\n{menu.options} ', 0, 5)
        if choice == 0: cart.budget = valid.get_valid_number('Enter your budget from 10 to 1000 USD! ', 10, 1000)
        elif choice == 1:
            if cart.budget:
                item_name = valid.get_valid_string(f'Enter the name of the items from {options} options! ', *options)
                item_price = valid.get_valid_number('Enter the price of the item from 1 to 100 USD! ', 1, 100)
                max_amount = int(cart.budget / item_price)
                amount_to_buy = valid.get_valid_number(f'Enter the amount of the item from 0 to {max_amount}! ', 0, max(0, max_amount))            
                cart.add_item(item_name, item_price, amount_to_buy)
                print('Item added successfully.')
            else: print('Please set up your budget first! ')
        elif choice == 2: print(cart.cart)
        elif choice == 3: cart.remove_item(valid.get_valid_string(f'Enter the name of the items from {options} options! ', *options))
        elif choice == 4: print(f'Your current budget available is {cart.budget} USD.')
        elif choice == 5: print('Thank you for choosing us! Good bye! '); return
        
if __name__ == '__main__': main()
