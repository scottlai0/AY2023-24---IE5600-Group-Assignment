class Vertex:
    
    def __init__(self, name):
        self.name = name
        self.adjacentList = []

    def addNeighbour(self, neighbour, weight=0):        
        neighbourExist = False

        for adjacentItem in self.adjacentList:
            if adjacentItem['vertex'].name == neighbour.name:
                neighbourExist = True
                break

        if not neighbourExist:
            self.adjacentList.append({'vertex': neighbour, 'distance': weight})
    
    def toString(self):    
        strData = str(self.key)
    
        for adjacentVertex in self.adjacentList:        
            strData += ' -> ' + str(adjacentVertex['vertex'].key) + ':' + str(adjacentVertex['distance'])

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

import string

if __name__ == "__main__":
    sample_graph = Graph()
    start_point = Vertex('Start Point')
    sample_graph.addVertex(start_point)
    print('Start point created and added to graph')
    
    # Generate vertices from A to V
    for letter in list(string.ascii_lowercase)[:-4]:
        exec(f"""vertex_{letter.upper()} = Vertex('{letter}')""")
        exec(f"""sample_graph.addVertex(vertex_{letter.upper()})""")
        print(f"""Vertex {letter.upper()} created and added to graph.""")
    
    