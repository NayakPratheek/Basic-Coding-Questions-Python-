# Creation and insertion of elements in Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    # Traversal Operation    
    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end =" ")
                n = n.ref

    # Insertion of elements at the beginning
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    #Insertion of element at the end 
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
        

LL1 = LinkedList()
LL1.insert_at_beginning(20)
LL1.insert_at_beginning(10)
LL1.insert_at_end(30)
LL1.insert_at_end(40)
LL1.printLL()
