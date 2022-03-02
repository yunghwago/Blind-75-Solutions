# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        recursive solution
        
        given a linked list 1(head)->2->3 what are our subproblems
        
        calling the recursion on 1, our head, will call a function to reverse 2->3
        calling the recursion on that will call a function to reverse 3, 
        and calling a recursion on that will call a function to reverse null, which is our stopping case/base case
        
        so what do we do in the recursion itself?
        set the end of the list to point to null, because we don't have access to the previous node within the recursion
        as we recurse upwards, set the current node to point to the previous node
        we also need to keep track of the new head of the list as we do this
        
        so for the list 1->2->3, at the last recursive call we will have 1->2->3, 3->null
        then 3->2->null, 1->2
        then 3->2->1->null, which is the list we want to return
        """
        
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next) #not sure how newHead doesn't get overwritten here by head all the time, like shouldn't newHead be 1 at the end? need to ask drew
            head.next.next = head
        head.next = None
        return newHead
