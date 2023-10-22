class LocationNode:
    lattitude = None
    longitude = None

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



class FoodItem:
    def __init__(self, item_name, price) -> None:
        self.item_name = item_name
        self.price = price

class Drink(FoodItem):
    def __init__(self, item_name, price) -> None:
        super().__init__(item_name, price)

if __name__ == "__main__":
    print('Hello World')