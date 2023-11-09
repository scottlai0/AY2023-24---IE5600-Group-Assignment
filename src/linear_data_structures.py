class Queue:
    
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