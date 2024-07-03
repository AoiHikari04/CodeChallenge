class Node:
    data = None
    nextNode = None

    def __init__(self, Data):
        self.data = Data
        self.nextNode = None

class PriorityQueue:
    def __init__(self):
        self.Head = None

    def add(self, data):
        newNode = Node(data)
        
        if self.Head is None:
            self.Head = newNode
            return
        
        temp = self.Head
        i = 0
        while temp is not None:
            prev = temp

            if temp.data > data:
                self._add(data, i)
                break

            temp = temp.nextNode
            i += 1
        
        if temp is None:
            prev.nextNode = newNode
            


    def _add(self, data, index):
        temp = self.Head
        newNode = Node(data)

        i = 0
        prev = None
        while temp is not None and i is not index:
            prev = temp
            temp = temp.nextNode
            i += 1

        if prev is None:
            newNode.nextNode = temp
            self.Head = newNode
            return
        
        prev.nextNode = newNode
        newNode.nextNode = temp
        

    def display(self):
        temp = self.Head

        while temp is not None:
            print(temp.data)
            temp = temp.nextNode

def main():
    pq = PriorityQueue()

    pq.add(15)
    pq.add(12)
    pq.add(30)
    pq.add(55)
    pq.add(13)
    pq.add(7)
    pq.display()

main()      
        

