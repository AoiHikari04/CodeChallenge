class Node:
    data = None

    def __init__(self, Data):
        self.data = Data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, data):
        newNode = Node(data)

        if self.root is None:
            self.root = newNode
            return
        
        temp = self.root

        while temp is not None:
            if data < temp.data:
                prev = temp
                temp = temp.left

            elif data > temp.data:
                prev = temp
                temp = temp.right

            else:
                print("Duplicate found")
                return
            
        if data < prev.data:
            prev.left = newNode
        elif data > prev.data:
            prev.right = newNode

    def remove(self, target):
        temp = self.root
        prev = None

        while temp is not None:
            if target < temp.data:
                prev = temp
                temp = temp.left
            elif target > temp.data:
                prev = temp
                temp = temp.right
            else:
                break

        if temp is None:
            print("Target not found")
            return
        
        
        #target node doesnt have child
        if temp.left is None and temp.right is None:
            if target < prev.data:
                prev.left = None
                return
            elif target > prev.data:
                prev.right = None
                return

        #if target doesnt have left child
        if temp.left is None:
            if target < prev.data:
                prev.left = temp.right
                temp.right = None
                return
            elif target > prev.data:
                prev.right = temp.right
                temp.right = None
                return
            

        rightmost = temp.left
        prevRight = temp
        while rightmost.right is not None:
            prevRight = rightmost
            rightmost = rightmost.right

        # Replace temp.data with rightmost.data
        temp.data = rightmost.data

        # Delete the rightmost node
        if prevRight.left == rightmost:
            prevRight.left = rightmost.left
        else:
            prevRight.right = rightmost.left

            



    def PostOrder(self, root):

        if root is not None:
            self.PostOrder(root.right)
            self.PostOrder(root.left)
            print(root.data)
            

    def postOrder(self):
        self.PostOrder(self.root)


def main():
    bst = BST()

    bst.add("mewo")
    bst.add("meow")
    bst.add("magnetic")
    bst.add("letsgooo")

    bst.remove("mewo")

    bst.postOrder()
                
main()


