class Node:
    name: str
    next: list
    
    def __init__(self, name):
        self.name = name
        self.next = []

    def addPath(self, nextNode: Node, distance: int):
        self.nextNode.append({nextNode: distance})
    
    def toString(self):
        if len(self.nextNode) == 0:
            print(f"{self.name} is a sink.")
        else:
            print(f"{self.name}")


class Queue():
    
    def __init__(self):
        self._items = list([])
       
    
    def empty(self):
        return self.size() == 0
    
    
    def size(self): 
        return len(self._items)                
    

    def enqueue(self, x):        
        self._items.insert(0, x)
    
    
    def dequeue(self):        
        if not self.empty():            
            return self._items.pop()    
        return None
    
    
    def toString(self):        
        return str(self._items)


if __name__ == "__main__":
    print('Hello World')