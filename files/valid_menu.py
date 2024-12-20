class Valid:
    def get_valid_number(self, prompt: str, min_val: int, max_val: int) -> int:
        while True:
            try:
                value = int(input(prompt))
                if min_val <= value <= max_val:
                    return value
                print('Invalid number! ')
            except ValueError:
                print('Invalid value! ')
            
    def get_valid_string(self, prompt: str, *args) -> str:
        while True:
            value = input(prompt).lower()
            if value in args:
                return value
            print('Invalid value! ')

class Menu:
    def __init__(self) -> None:
        self.__options = dict(enumerate(['Set budget', 'Add item', 'View cart', 'Remove item', 'View budget', 'Exit']))
    
    @property
    def options(self) -> dict:
        return self.__options
    
    @options.setter
    def options(self, new_val: dict) -> None:
        self.__options = new_val