from valid_menu import Valid, Menu
from budget_cart import Cart

class Store:
    def __init__(self) -> None:
        self.store = {'apple':4, 'orange':6, 'lemon':4, 'pineapple':4, 'banana':6, 'cherry':8, 'blackberry':10}
    
    @property
    def items_for_sale(self) -> dict:
        return self.store
    
class Purchase:
    
    def __init__(self) -> None:
        self.valid = Valid()
        self.menu = Menu()
        self.store = Store()
        self.cart = Cart()

    def set_budget(self) -> None:
        self.cart.balance = self.valid.get_valid_number('Set your Budget from 10 to 1000 USD! ', 10, 1000)

    def add_item(self) -> None:
        item_name = self.valid.get_valid_string(f'Enter the name of the Item from {self.store.items_for_sale} store! ', *self.store.items_for_sale.keys())
        item_price = self.store.items_for_sale[item_name]
        max_amount = int(self.cart.balance / item_price)
        if max_amount > 0:
            amount_to_buy = self.valid.get_valid_number(f'Enter the quantity of the Item to buy from 0 to {max_amount}! ', 0, max(0, max_amount))
            self.cart.add_item(item_name, item_price, amount_to_buy)
            print('Item added successfully! ')
        else: print('You cannot add item because you have run out of budget! ')

    def view_cart(self) -> None: 
        print(self.cart.to_purchase)

    def remove_item(self) -> None:
        item_names = [item['item_name'] for item in self.cart.to_purchase]
        item_to_remove = self.valid.get_valid_string(f'Enter the ame of the Item from {item_names} actual Cart to remove! ', *item_names)
        max_quantity = [item['quantity_to_buy'] for item in self.cart.to_purchase if item['item_name'] == item_to_remove]
        quantity_to_remove = self.valid.get_valid_number(f'Enter the quantity (0-{max_quantity[0]}) to remove from the Cart! ', 0, max_quantity[0])
        self.cart.remove_item(item_to_remove, quantity_to_remove)
        print('Item deleted successfully! ')
    
    def view_budget(self) -> None: 
        print(f'Your current Budget available is {self.cart.balance} USD. ')

    @staticmethod
    def exit() -> None:
        print('Thank you for choosing us! Good bye! ')
    
    def actions_(self) -> dict:
        actions = {
            0: lambda: self.set_budget(),
            1: lambda: self.add_item() if self.cart.balance else print('Please set up your Budget first! '),
            2: lambda: self.view_cart(),
            3: lambda: self.remove_item() if self.cart.to_purchase else print('You cannot remove Item because your Cart is Empty! '),
            4: lambda: self.view_budget(), 
            5: lambda: exit()}
        return actions

    def menu_(self) -> int:
        return self.valid.get_valid_number(f'Choose your option from the menu below!\n{self.menu.options} ', 0, 5)