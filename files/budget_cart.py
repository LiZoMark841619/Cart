class Budget:    
    def __init__(self) -> None:
        self._budget = 0
    @property
    def budget(self) -> int:
        return self._budget
    
    @budget.setter 
    def budget(self, new_val: int) -> None:
        self._budget = new_val

class Cart(Budget):
    cart: list[dict] = []
    
    def add_item(self, item_name: str, item_price: int, amount_to_buy: int) -> None:
        item = {'item_name':item_name, 'item_price':item_price, 'amount_to_buy':amount_to_buy}
        Cart.cart.append(item)
        self.budget -= item_price * amount_to_buy
            
    def remove_item(self, item_name: str) -> None:
        item_name = item_name.lower()
        for item in Cart.cart:
            if item_name == item['item_name']:
                Cart.cart.remove(item)
                self.budget += item['item_price'] * item['amount_to_buy']
                print('Item deleted successfully! ')
            else:
                print('Item not found in the cart! ')