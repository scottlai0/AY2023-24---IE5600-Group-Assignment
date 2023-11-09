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
        strData = str(self.name)
    
        for adjacentVertex in self.adjacentList:        
            strData += ' -> ' + str(adjacentVertex['vertex'].name) + ':' + str(adjacentVertex['distance'])

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
import pickle

def generateMapOfLumbridgeAndAlKharid() -> Graph:
    sample_graph = Graph()
    print('> Creating Vertices...')
    sample_graph.addVertex('start_point')
    print('Vertex start_point created. and added to graph.')
    
    # Generate vertices from A to V
    for letter in list(string.ascii_lowercase)[:-5]:
        exec(f"""sample_graph.addVertex('{letter.upper()}')""")
        print(f"""Vertex {letter.upper()} created. and added to graph.""")
    print()
    print('> Creating Edges...')
    print('Start Point <-> A edge created.')
    sample_graph.addEdge('start_point','A', 5)
    sample_graph.addEdge('A','start_point', 5)
    
    print('V <-> A edge created.')
    sample_graph.addEdge('A','U', 10)
    sample_graph.addEdge('U','A', 10)

    print('M <-> A edge created.')
    sample_graph.addEdge('A','M', 30)
    sample_graph.addEdge('M','A', 30)
    
    print('U <-> T edge created.')
    sample_graph.addEdge('U','T', 55)
    sample_graph.addEdge('T','U', 55)
    
    print('B <-> A edge created.')
    sample_graph.addEdge('A','B', 10)
    sample_graph.addEdge('B','A', 10)

    print('M <-> N edge created.')
    sample_graph.addEdge('M','N', 25)
    sample_graph.addEdge('N','M', 25)
    
    print('N <-> T edge created.')
    sample_graph.addEdge('N','T', 65)
    sample_graph.addEdge('T','N', 65)
    
    print('M <-> O edge created.')
    sample_graph.addEdge('M','O', 30)
    sample_graph.addEdge('O','M', 30)
    
    print('M <-> L edge created.')
    sample_graph.addEdge('M','L', 40)
    sample_graph.addEdge('L','M', 40)

    print('O <-> P edge created.')
    sample_graph.addEdge('O','P', 5)
    sample_graph.addEdge('P','O', 5)

    print('Q <-> O edge created.')
    sample_graph.addEdge('O','Q', 15)
    sample_graph.addEdge('Q','O', 15)    
    
    print('O <-> R edge created.')
    sample_graph.addEdge('O','R', 20)
    sample_graph.addEdge('R','O', 20)
    
    print('Q <-> R edge created.')
    sample_graph.addEdge('Q','R', 10)
    sample_graph.addEdge('R','Q', 10)
    
    print('P <-> R edge created.')
    sample_graph.addEdge('P','R', 12)
    sample_graph.addEdge('R','P', 12)
    
    print('R <-> S edge created.')
    sample_graph.addEdge('R','S', 35)
    sample_graph.addEdge('S','R', 35)
    
    print('S <-> T edge created.')
    sample_graph.addEdge('S','T', 20)
    sample_graph.addEdge('T','S', 20)
    
    print('T <-> L edge created.')
    sample_graph.addEdge('T','L', 25)
    sample_graph.addEdge('L','T', 25)
    
    print('L <-> H edge created.')
    sample_graph.addEdge('L','H', 55)
    sample_graph.addEdge('H','L', 55)
    
    print('L <-> K edge created.')
    sample_graph.addEdge('L','K', 50)
    sample_graph.addEdge('K','L', 50)
    
    print('K <-> H edge created.')
    sample_graph.addEdge('H','K', 10)
    sample_graph.addEdge('K','H', 10)
    
    print('D <-> H edge created.')
    sample_graph.addEdge('H','D', 20)
    sample_graph.addEdge('D','H', 20)
    
    print('G <-> H edge created.')
    sample_graph.addEdge('H','G', 8)
    sample_graph.addEdge('G','H', 8)
    
    print('J <-> K edge created.')
    sample_graph.addEdge('K','J', 15)
    sample_graph.addEdge('J','K', 15)
    
    print('L <-> H edge created.')
    sample_graph.addEdge('I','J', 8)
    sample_graph.addEdge('J','I', 8)
    
    print('K <-> I edge created.')
    sample_graph.addEdge('K','I', 8)
    sample_graph.addEdge('I','K', 8)
    
    print('K <-> G edge created.')
    sample_graph.addEdge('K','G', 12)
    sample_graph.addEdge('G','K', 12)
    
    print('G <-> I edge created.')
    sample_graph.addEdge('G','I', 5)
    sample_graph.addEdge('I','G', 5)
    
    print('G <-> F edge created.')
    sample_graph.addEdge('F','G', 5)
    sample_graph.addEdge('G','F', 5)
    
    print('G <-> E edge created.')
    sample_graph.addEdge('E','G', 15)
    sample_graph.addEdge('G','E', 15)
    
    print('D <-> F edge created.')
    sample_graph.addEdge('D','F', 10)
    sample_graph.addEdge('F','D', 10)
    
    print('D <-> E edge created.')
    sample_graph.addEdge('D','E', 5)
    sample_graph.addEdge('E','D', 5)
    
    print('D <-> C edge created.')
    sample_graph.addEdge('C','D', 20)
    sample_graph.addEdge('D','C', 20)
    
    print('B <-> C edge created.')
    sample_graph.addEdge('C','B', 15)
    sample_graph.addEdge('B','C', 15)
    
    print('B <-> L edge created.')
    sample_graph.addEdge('L','B', 60)
    sample_graph.addEdge('B','L', 60)
    
    return sample_graph

if __name__ == "__main__":
    sample_graph = generateMapOfLumbridgeAndAlKharid()
    with open('../data/sample_graph.map','wb+') as f:
        pickle.dump(sample_graph, f)
        print('> Saved Graph.')
    f.close()