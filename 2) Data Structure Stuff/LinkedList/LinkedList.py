class Node:
        data = None
        nextNode = None

        def __init__(self, Data):
            self.data = Data
            self.nextNode = None


class linkedList:

    def __init__(self):
        self.Head = None

    def add(self, data):
        newNode = Node(data)

        if self.Head is None:
            self.Head = newNode
            return 
        
        temp = self.Head
        while temp.nextNode != None:
            temp = temp.nextNode

        temp.nextNode = newNode

    def display(self):
        temp = self.Head

        while temp != None:
            print(temp.data)
            temp = temp.nextNode

    def removeLast(self):
        temp = self.Head

        while temp.nextNode:
            lastTemp = temp
            temp = temp.nextNode
        
        lastTemp.nextNode = None

    def remove(self, data):
        temp = self.Head

        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.nextNode

        if temp is None:
            print("Not Found")
            return
        
        prev.nextNode = temp.nextNode
        temp.nextNode = None

        return temp.data
            



def Main():
    ll = linkedList()

    ll.add('Ahmad')
    ll.add("Meow")
    ll.add("yow")
    ll.display()
    print()

    ll.removeLast()
    ll.display()
    print()

    ll.add("Come")
    ll.add("Take")
    ll.remove("Meow")
    ll.display()
    

Main()



    

    