class Vertex:
    data = None
    nextNode = None

    def __init__(self, Data):
        self.data = Data
        self.nextNode = None
        self.AdjenciesList = {}

class Edge:
    def __init__(self, weight, toVertex):
        self.weight = weight
        self.toVertex = toVertex

class Graph:
    def __init__(self):
        self.Head = None
    
    def addVertex(self, data):
        newVertex = Vertex(data)

        if self.Head is None:
            self.Head = newVertex
            return

        if self.hadVertex(data):
            print("duplicate vertex " + data)
            return
        
        newVertex.nextNode = self.Head
        self.Head = newVertex

    def addEdge(self, source, dest, weight):
        if not self.hadVertex(source) or not self.hadVertex(dest):
            return
        
        temp = self.Head

        while temp.data is not source:
            temp = temp.nextNode
        
        tempTarget = self.Head

        while tempTarget.data is not dest:
            tempTarget = tempTarget.nextNode
        
        temp.AdjenciesList[tempTarget] = weight
        
    def hadVertex(self, data):
        temp = self.Head

        while temp is not None:
            if temp.data == data:
                return True
            
            temp = temp.nextNode
        
        return False

