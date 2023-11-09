class Person:
    def __init__(self, id: str, gender: str):
        self.id = id
        self.gender = gender
    
    def getID(self):
        return self.id
    
    def getGender(self):
        return self.gender

    

class Customer(Person):
    def __init__(self, id: str, gender: str, address):
        super().__init__(id, gender)
        self.address = address
        
    def getAddress(self):
        return self.address
    
    def toString(self):
        return f"""{self.getID()} - {self.getGender()} - Vertex {self.getAddress().name}"""
        

class Courier(Person):
    orderList = []
    max_order_capacity: int
    
    def __init__(self, id: str, gender: str, age: int, max_order_capacity: int):
        super().__init__(id, gender)
        self.age = age
        self.max_order_capacity = max_order_capacity
                
    def getAge(self):
        return self.age
    
    def assignOrder(self, order):
        if len(self.orderList) < self.max_order_capacity:
            self.orderList.append(order)
        return
    
    def getMaxOrderCapacity(self):
        return self.max_order_capacity
    
    def toString(self):
        nl = '\n'
        return f"id: {self.getID()}{nl}Gender: {self.getGender()}{nl}Age: {self.getAge()}{nl}Max Order Carrying Capacity: {self.getMaxOrderCapacity()}"
        