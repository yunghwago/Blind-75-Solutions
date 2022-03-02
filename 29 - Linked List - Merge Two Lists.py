# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        instinct
        have a pointer start at the head of l1, and the head of l2, and keep track of the end of the new linked list we want to return
        compare the values of both pointers, 
        scenarios:
        1. if they are equal:
        take value from l1, increment l1 pointer
        2. l1 pointer smaller than l2:
        set head l1 to point to head l2, and update end of new list, increment head l1 pointer
        3. head l2 is smaller than head l1:
        set head l2 to point to head l1, and update end of new list, increment head l2 pointer
        
        how do we handle one of the pointers reaching None before the other pointer
        the list is sorted, so we can just take the rest of that list and insert it into our output
        """
        output = ListNode() #output has to be initialized to dummy value first to avoid edge case of intial empty list
        tail = output #keep track of the last node inserted into our output to compare to l1 l2
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        #handle lists of unequal length
        if list1:
            tail.next = list1 #no need to append each individual node of list1, since we can just append the head to our output, and it already points to all the right things
        if list2:
            tail.next = list2
                
        return output.next #to ignore the dummy value inserted initially
