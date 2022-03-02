# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        would it make sense to get the tail of the list, and move back n times until the node is found?
        no, because we can't move back in a singly linked list
        
        we know that we need to keep track of the node that comes directly before the node to be removed, and the node that comes directly after it
        to redirect the linked list pointers
        
        solution: 2 pointer solution
        if we have 2 pointers spaced n (which in this case is 2) nodes apart, and iterate through the list, it'll look like this
        1->2->3->4->5->None
                 L      R
        which is great because now L is pointing at the node we need to remove, but we don't have anything pointing at 3 to redirect it
        to solve this we can insert a dummy node, and have it point to 1, causing our 2 pointers to be n+1 nodes apart
        iterating through that list will look like this:
        dummy -> 1->2->3->4->5->None
                       L         R
        we can just use L.next to access 4 to delete it, and return dummy.next to return the full list
                 
        """
        
        dummy = ListNode(0, head) #value of dummy node actually doesn't matter and could be anything
        L = dummy
        R = head
        #space 2 pointers apart as needed
        for i in range(n):
            R = R.next
        while R != None:
            L = L.next
            R = R.next
        L.next = L.next.next
        return dummy.next
