# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        solution: we need to split the list in half, then reverse the right half of the list.
        why do we need to reverse the right half of the list? so that it's contents are accessible from the end of the list
        
        how do we split the list in two?
        or rather, how do we detemine the middle point of the list?
        sol: fast and slow pointer
        if we initialize a fast and slow pointer at the head.next and head of the list respectively, and have the fast pointer move 2 nodes for every node the slow pointer moves,
        the slow pointer will end up at the halfway mark
        
        ex.
        1->2->3->4
        S  F
        1->2->3->4
           S     F
           
        now we have to account for odd lengths of lists, because F will end up at null instead of the end of the list
        ex.
        1->2->3->4->5->None
              S     F
        """
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #beginning of second half of the list
        previous = None # previous node tracker, used to keep track in reversing this list
        slow.next = None #actually split the lists into two different lists
        
        #reverse the second list
        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp
            
        #actually merge two halves of the list
        second = previous #second will be None at the end of our last while loop, and previous is actually the new head of the list
        first = head
        while second: #second is guaranteed to either be shorter or equal to length than our first list
            #for odd operations, the last node of second will point to the last node in first
            #for even operations, the last node of second will point to the next of the last node in first, which is None
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
