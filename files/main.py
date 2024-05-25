from item_budget import Valid, Menu, Item

def main():
    valid, menu, purchase = Valid(), Menu(), Item()
    while True:
        choice = valid.get_valid_number(f'Choose your option from the menu below!\n{menu.options} ', 0, 5)
        if choice == 0: purchase.budget = valid.get_valid_number('Enter your budget from 10 to 1000 USD! ', 10, 1000)
        elif choice == 1:
            options = ['apple', 'orange', 'lemon', 'pineapple', 'banana', 'cherry', 'blackberry']
            name = valid.get_valid_string(f'Enter the name of the items from {options} options! ', *options)
            price = valid.get_valid_number('Enter the price of the item from 1 to 100 USD! ', 1, 100)
            max_amount = int(purchase.budget / price)
            amount = valid.get_valid_number(f'Enter the amount of the item from 0 to {max_amount}! ', 0, max(0, max_amount))            
            purchase.item = [name, price, max_amount, amount]
            purchase.add_item()
            print('Item added successfully.')
        elif choice == 2: print(purchase.cart)
        elif choice == 3: purchase.remove_item()
        elif choice == 4: print(f'Your current budget available is {purchase.budget} USD.')
        elif choice == 5: print('Good bye! '); return
if __name__ == '__main__': main()