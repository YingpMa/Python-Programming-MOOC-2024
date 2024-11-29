# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.max_weight:
            self.items.append(item)

    def __str__(self):
        if len(self.items) == 1:
            return f"1 item ({self.weight()} kg)"
        else:
            return f"{len(self.items)} items ({self.weight()} kg)"
        
    def weight(self):
        weight = 0
        for item in self.items:
            weight += item.weight()
        return weight

    def print_items(self):
        for item in self.items:
            print(item)
    def heaviest_item(self):
        heaviest = 0
        heaviest_item = None
        if self.items == []:
            return None
        for item in self.items:
            if item.weight() > heaviest:
                heaviest = item.weight()
                heaviest_item = item
        
        return heaviest_item

class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.space = max_weight
        self.items = []

    def add_suitcase(self, item: Suitcase):
        if self.space >= item.weight():
            self.space -= item.weight()
            self.items.append(item)

    def __str__(self):
        if len(self.items) == 1:
            return f"1 suitcase, space for {self.space} kg"
        else:
            return f"{len(self.items)} suitcases, space for {self.space} kg"
        
    def print_items(self):
        for item in self.items:
            item.print_items()


if __name__ == "__main__":

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()