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
    
    def add_item(self, item_name: str, item_price: int, quantity_to_buy: int) -> None:
        Cart.to_purchase.append(
            {'item_name':item_name,
            'item_price':item_price,
            'quantity_to_buy':quantity_to_buy,
            'total':item_price*quantity_to_buy
            })
        self.budget -= item_price * quantity_to_buy

    def remove_item(self, item_name: str, quantity_to_remove: int) -> None:
        for item in Cart.to_purchase:
            if item_name.lower() == item['item_name']:
                item['quantity_to_buy'] -= quantity_to_remove
                self.budget += item['item_price'] * quantity_to_remove