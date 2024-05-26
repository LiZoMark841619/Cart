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
    
    def add_to_cart(self) -> dict:
        return {'item_name':self._item_name, 'item_price':self._item_price, 'amount_to_buy':self._amount_to_buy}
    add_to_cart = property(add_to_cart)
    
    @add_to_cart.setter 
    def add_to_cart(self, new_vals: list) -> None:
        self._item_name, self._item_price, self._max_amount, self._amount_to_buy = new_vals
        Item.cart.append(self.add_to_cart)
        self._budget = self.budget - self.add_to_cart['item_price'] * self.add_to_cart['amount_to_buy']
    
    @add_to_cart.deleter
    def add_to_cart(self) -> None:
        if not Item.cart: print('There is no item in the cart yet! Choose - Add item - from the menu by typing 1! ')
        else:
            delete_item = input('Enter the item you would like to remove! ').lower()
            for item in Item.cart:
                if delete_item == item['item_name']:
                    Item.cart.remove(item)
                    self._budget = self.budget + item['item_price'] * item['amount_to_buy']
                    print('Item deleted successfully! ')