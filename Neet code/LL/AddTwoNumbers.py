# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #creating an instance of a node, a dummy node, so that we don't have to deal with the cases of inserting into a linked list
        curr = dummy #current pointer is going to be pointing at where we will be inserting a new node

        carry = 0
        while l1 or l2 or carry: #iterating through each linked list and carry while they're not null
        #one of the lists may be null so we're gonna get the digits from them if so
            v1 = l1.val if l1 else 0 #get the value of l1 if it is not null. if it is, we set it to 0
            # same for l2
            v2 = l2.val if l2 else 0

            #now lets add the two digits stored in the lists
            val = v1 + v2 + carry
            # but what if we get a new carry other than 0?
            # if carry is two digits
            carry = val // 10
            #now we mod the value to get the ones place digit
            val = val % 10
            #so now
            curr.next = ListNode(val)

            #update pointers
            curr = curr.next
            #and l1 and l2 if they're not null
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next #return the list we just created


        
        