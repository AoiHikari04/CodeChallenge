class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class Stack:
    def __init__(self):
        self.Head = None

    def add(self, data):
        newNode = Node(data)

        if self.Head == None:
            self.Head = newNode
            return
        
        temp = self.Head

        while temp.nextNode:
            temp = temp.nextNode

        temp.nextNode = newNode

    def peek(self):
        temp = self.Head

        while temp.nextNode:
            temp = temp.nextNode
        
        return temp.data
    
    def pop(self):
        temp = self.Head

        while temp.nextNode:
            prev = temp
            temp = temp.nextNode

        prev.nextNode = None

        return temp.data
    
    def display(self):
        temp = self.Head

        while temp:
            print(temp.data)
            temp = temp.nextNode
    

def Main():

    stck = Stack()

    stck.add("Ahmad")
    stck.add(2)
    stck.add(5)
    stck.add(3)
    stck.display()
    print()

    print(stck.peek())
    stck.display()
    print()

    stck.pop()
    stck.display()

Main()





        


        

