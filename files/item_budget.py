class Valid:
    def get_valid_number(self, prompt: str, min_val: int, max_val: int) -> int:
        while True:
            try:
                value = int(input(prompt))
                if min_val <= value <= max_val: return value
                print('Invalid number! ')
            except ValueError: print('Invalid value! ')
            
    def get_valid_string(self, prompt: str, *args) -> str:
        while True:
            value = input(prompt).lower()
            if value in args: return value
            print('Invalid value! ')

class Menu:
    def __init__(self) -> None:
        self._options = {0:'Set budget', 1:'Add item', 2:'View cart', 3:'Remove item', 4:'View budget', 5:'Exit'}
    
    def options(self) -> int:
        return self._options
    options = property(options)
    
    @options.setter
    def options(self, new_val: dict) -> None:
        self._options = new_val
        
class Budget:    
    def __init__(self) -> None:
        self._budget = 0
    
    def budget(self) -> int:
        return self._budget
    budget = property(budget)
    
    @budget.setter 
    def budget(self, new_val: int) -> None:
        self._budget = new_val

class Item(Budget):
    cart: list[dict] = []
    
    def item(self) -> dict:
        return {'item_name':self._item_name, 'item_price':self._item_price, 'amount_to_buy':self._amount_to_buy}
    item = property(item)
    
    @item.setter 
    def item(self, new_vals: list) -> None:
        self._item_name, self._item_price, self._max_amount, self._amount_to_buy = new_vals
    
    def add_item(self) -> None:
        item = self.item
        Item.cart.append(item)
        self._budget = self.budget - item['item_price'] * item['amount_to_buy']
    
    def remove_item(self) -> None:
        if not Item.cart: print('There is no item in the cart yet! Choose - Add item - from the menu by typing 1! ')
        else:
            delete_item = input('Enter the item you would like to remove! ').lower()
            for item in Item.cart:
                if delete_item == item['item_name']:
                    Item.cart.remove(item)
                    self._budget = self.budget + (item['item_price'] * item['amount_to_buy'])
                    print('Item deleted successfully! ')