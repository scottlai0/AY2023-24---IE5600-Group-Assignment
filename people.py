class Person:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender
    
    def getName(self):
        return self.name
    
    def getGender(self):
        return self.gender

    

class Customer(Person):
    def __init__(self, name: str, gender: str, address):
        super().__init__(name, gender)
        self.address = address
        
    def getAddress(self):
        return self.address
    
    def toString(self):
        return f"""{self.getName()} - {self.getGender()} - Vertex {self.getAddress().name}"""
        

class Courier(Person):
    orderList = []
    max_order_capacity: int
    
    def __init__(self, name: str, gender: str, age: int, max_order_capacity: int):
        super().__init__(name, gender)
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
        return f"Name: {self.getName()}{nl}Gender: {self.getGender()}{nl}Age: {self.getAge()}{nl}Max Order Carrying Capacity: {self.getMaxOrderCapacity()}"
        