class Budget:    
    def __init__(self) -> None:
        self.__budget = 0
    
    def __str__(self) -> str:
        return f'{self.__budget}'

class Item:
    def __init__(self, item_name: str, item_price: int, quantity_to_buy: int) -> None:
        self.item_name = item_name
        self.item_price = item_price
        self.quantity_to_buy = quantity_to_buy
        self.total = item_price * quantity_to_buy

class Cart:
    def __init__(self) -> None:
        self.balance = Budget()
        self.to_purchase = []

    def add_item(self, item_name: str, item_price: int, quantity_to_buy: int) -> None:
        item = Item(item_name, item_price, quantity_to_buy)
        self.to_purchase.append(item.__dict__)
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