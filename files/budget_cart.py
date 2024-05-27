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
    to_purchase: list[dict] = []
    
    def add_item(self, item_name: str, item_price: int, amount_to_buy: int) -> None:
        item = {'item_name':item_name, 'item_price':item_price, 'amount_to_buy':amount_to_buy}
        Cart.to_purchase.append(item)
        self.budget -= item_price * amount_to_buy
            
    def remove_item(self, item_name: str) -> None:
        for item in Cart.to_purchase:
            if item_name.lower() == item['item_name']:
                Cart.to_purchase.remove(item)
                self.budget += item['item_price'] * item['amount_to_buy']
                print('Item deleted successfully! ')
            else:
                print('Item not found in the cart! ')