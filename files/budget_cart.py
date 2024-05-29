class Budget:    
    def __init__(self) -> None:
        self._budget = 0
    
    @property
    def balance(self) -> int:
        return self._budget
    
    @balance.setter 
    def balance(self, new_val: int) -> None:
        self._budget = new_val

class Cart(Budget):
    def __init__(self) -> None:
        super().__init__()
        self.to_purchase = []
            
    def add_item(self, item_name: str, item_price: int, quantity_to_buy: int) -> None:
        self.to_purchase.append(
            {'item_name':item_name, 'item_price':item_price, 'quantity_to_buy':quantity_to_buy, 'total':item_price*quantity_to_buy})
        self.update_balance(-item_price * quantity_to_buy)

    def remove_item(self, item_name: str, quantity_to_remove: int) -> None:
        for item in self.to_purchase:
            if item_name.lower() == item['item_name']:
                if quantity_to_remove == item['quantity_to_buy']:
                    self.to_purchase.remove(item)
                else:
                    item['quantity_to_buy'] -= quantity_to_remove
                    item['total'] = item['item_price'] * item['quantity_to_buy']
                self.update_balance(item['item_price'] * quantity_to_remove)

    def update_balance(self, amount: int) -> None:
        self.balance += amount