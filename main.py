class LocationNode:
    lattitude: float = None
    longitude: float = None

    def __init__(self, lattitude, longitude) -> None:
        self.lattitude = lattitude
        self.longitude = longitude

class Menu:

    feedback = []
    def __init__(self, name, address, start_time = None, end_time = None) -> None:
        self.name = name
        self.address = address
        self.start_time = start_time
        self.end_time = end_time

    def addComment(self, comment: str) -> None:
        comment_id = len(self.feedback) + 1
        self.feedback.append({comment_id: comment})


class MenuItem:
    def __init__(self, item_name, price) -> None:
        self.item_name = item_name
        self.price = price

class Food(MenuItem):
    def __init__(self, item_name, price) -> None:
        super().__init__(item_name, price)

class Drink(MenuItem):
    def __init__(self, item_name, price) -> None:
        super().__init__(item_name, price)


class Cart:
    items: list = []

    def addItem(self, menu_item: MenuItem, quantity: int = 1) -> None:
        item = {'name': menu_item, 'quantity': quantity}
        list.append(item)

    def updateQuantity(self, menu_item: MenuItem, quantity: int) -> None:
        for item in self.items:
            if item['name'] == menu_item:
                item['quantity'] = quantity
            break

    def deleteItem(self, menu_item: MenuItem) -> None:
        for item in self.items:
            if item['name'] == menu_item:
                self.items.remove(item)


if __name__ == "__main__":
    print('Hello World')