
class Vertex:
    
    def __init__(self, key):
        self.key = key
        self.adjacentList = list([])

    def addNeighbour(self, neighbour, weight=0):        
        neighbourExist = False

        for adjacentItem in self.adjacentList:
            if adjacentItem[0].key == neighbour.key:
                neighbourExist = True
                break

        if not neighbourExist:
            self.adjacentList.append((neighbour, weight))
    
    def toString(self):    
        strData = str(self.key)
    
        for adjacentVertex in self.adjacentList:        
            strData += ' -> ' + str(adjacentVertex[0].key) + ':' + str(adjacentVertex[1])

        return strData



class Graph():
    
    def __init__(self): 
        self.vertices = dict({})
        self.numVertices = 0
    
    def addVertex(self, key):  
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex  
        return newVertex

    
    def getVertex(self, key):  
        if key in self.vertices.keys():      
            return self.vertices[key]        
        return None
    
    
    def addEdge(self, fromKey, toKey, weight=0): 

        if not self.has_key(fromKey):     
            self.addVertex(fromKey)
        
        if not self.has_key(toKey):
            self.addVertex(toKey)
        
        self.vertices[fromKey].addNeighbour(self.vertices[toKey], weight)
    
    
    def getVertices(self): 
        return self.vertices.values()
    
    def has_key(self, key):  
        if key in self.vertices.keys():     
            return True
        return False



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


if __name__ == "__main__":
    print('Hello World')