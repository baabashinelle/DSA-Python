# Doubly linked list in Python
class Node:
    def __init__ (self,data):
        self.data = data
        # stores two address, previous and next
        self.nref = None
        self.pref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    #traversing in the forward direction
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->",end=" ")
                n = n.nref

    #traversing in the reverse direction
    def print_LL_reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->",end=" ")
                n = n.pref

    #inserting into an empty doubly linked list
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list is not empty")

    
    
    #insertion of node at the beginning of doubly linked list
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else :
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    #insertion of node at the end of doubly linked list
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
