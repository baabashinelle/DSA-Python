# Linked List implementation in Python
class Node:
    # creating a node
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next



#from amulya's academy
# create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None # ref is the address each node stores
# you can create individual nodes from the node class like so :
# node1 = Node(10)
# node2 = Node(20) etc. 
# at this point, they'll all not be linked since the ref property is none. so they dont have addresses
# to connect individual nodes, create another class to connect them

class LinkedList:
    def __init__(self):
        self.head = None
    # code all the methods of what u can do in a linkedlist
    # operations for traversal

    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->",end=" ")
                n = n.ref
    
    # adding elements at the beginning of the linked list
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # adding elements at the end of the linked list
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # adding elements between nodes after a node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # adding an element to an empty linked list
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("This linked list is not empty")


class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

node_a = Node(10)
node_b = Node(11)
node_c = Node(12)

# node_a.next = node_b
# node_b.next = node_c
# llist = Node(10, Node(20, Node(30, Node(40))))
# while llist:
#     print(llist.val)
#     llist = llist.next

# print(llist.val)
# print(node_a)

# """
#         |
#    A -> B -> C -> D -> None


# """
# from dataclasses import dataclass

# @dataclass
# class LinkedList:

#     def __init__(self, node):
#         self.weouow4 = node

#     @setattr
#     def set_head(self, v):
#         self.wewe = Node(v)
        

#     def get_head(self):
#         return self.head.val

#     # def _insert(self, v):
#     #     node = Node(v)
#     #     node.next = self.head
#     #     LinkedList.head = node

# llist = LinkedList(Node(10))
# #llist.insert(20)
# llist._head = node_a

# #llist.set_head(node_a)
# print(llist)

