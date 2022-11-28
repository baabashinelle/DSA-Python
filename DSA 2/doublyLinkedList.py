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