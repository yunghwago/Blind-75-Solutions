# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        keep track of numbers visited so far with list
        if head.next is pointing to a number within list, return True
        else false
        
        solution:
        instead of using a list to keep track of visited nodes, we have to use a hashset, because you technically can have duplicate values in a linked list
        like 3 -> 3        
        so we need to store the object itself in the hashset, instead of just the value
        
        alternatively we can use the tortoise and hare algorithm
        """
        slow, fast = head, head
        while fast and fast.next: #fast pointer can check for end of list for us first
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
