# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        let's say we have four lists:
        [5], [7], [3], and [8]
        
        iteratively merging our first two lists gives us [5,7]
        iteratively merging 3 into our output list gives us [3,5,7]
        but if we want to iteratively merge 8, we have to compare it to 3, then 5, then 7, and then insert it giving us [3,5,7,8]
        giving us a horrible runtime of O(k (number of lists) * n(average length of each list))
        
        
        instead we should be dividing and conquering
        what does that mean
        instead of merging [5] then [7] then [3] then [8], we can group our merges
        we can merge [5] and [7] and at the same time merge [3] and [8]
        giving us lists [5,7] and [3,8] then we can merge those two lists
        so we are just merging pairs of lists at a time, different from having a middle pointer and merging left and right halves
        
        because we end up having to run through less lists, by cutting the amount of lists in the search space by half every time
        this gives us a runtime of O(logk*n) or O(nlogk)
        
        """
        #handle edge case of no lists:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = [] #merged lists needs to be cleared on every pass through lists
            for i in range(0, len(lists), 2): #"2" here means we are iterating through our array 2 lists at a time
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None #list 2 will be out of bounds if we have an odd amount of lists and are incrementing by 2 at a time
                mergedLists.append(self.merge2Lists(l1, l2))
            lists = mergedLists
        return lists[0]
    
    def merge2Lists(self, list1, list2):
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
        
