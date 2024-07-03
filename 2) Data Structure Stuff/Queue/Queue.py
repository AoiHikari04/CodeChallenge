class Node:
    data = None
    nextNode = None

    def __init__(self, Data):
        self.data = Data
        self.nextNode = None

class Queue:
    def __init__(self):
        self.head = None

    def enQueue(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head

        while temp.nextNode is not None:
            temp = temp.nextNode

        temp.nextNode = newNode

    def deQueue(self):

        if self.head is None:
            print("No element")
            return
        
        temp = self.head
        self.head = temp.nextNode
        temp.nextNode = None

        return temp.data
    
    def display(self):
        
        temp = self.head
        
        while temp is not None:
            print(temp.data)
            temp = temp.nextNode


def main():

    q = Queue()

    q.enQueue("Ahmad")
    q.enQueue("mail")
    q.enQueue("Pakcik Sebelah Rumah")
    q.display()
    print()

    q.deQueue()
    q.deQueue()
    q.display()

           
main()