from graph import Vertex

class Person:
    def __init__(self, id: str, name: str, gender: str):
        self.id = id
        self.name = name
        self.gender = gender
    
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getGender(self):
        return self.gender

    

class Customer(Person):
    def __init__(self, id: str, name: str, gender: str, address: Vertex):
        super().__init__(id, name, gender)
        self.address = address
        
    def getAddress(self):
        return self.address
    
    def toString(self):
        return f"""Customer ID: {self.getID()}, Name: {self.getName()}, Gender: {self.getGender()}, Vertex: {self.getAddress().name}"""
        

class Courier(Person):
    max_order_capacity: int
    age: int
    max_order_capacity: int
    
    def __init__(self, id: str, name: str, gender: str, age: int, max_order_capacity: int):
        super().__init__(id, name, gender)
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
        return f"Courier ID: {self.getID()}, Name: {self.getName()}, Gender: {self.getGender()}, Age: {self.getAge()}, Max Order Carrying Capacity: {self.getMaxOrderCapacity()}"
        