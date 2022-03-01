class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        so the iterative solution that runs in O(n) time is really easy. iterate through the array and keep track of the min value as we're doing it:

        minReturn = 9999999999999999999999999
        for n in nums:
            if n < minReturn:
                minReturn = n
        return minReturn
    
        but we need a solution that has a runtime of O(log n), so how can we take advantage of the rotation of the array? if at all?
        
        a binary search runs in O(logn) time, and doing a binary search, and returning the first entry of the array WOULD be a solution, but that doesn't utilize the
        rotation aspect of the question at all.
        
        solution: we can say that a rotated array has two halves. the array [3,4,5,1,2] can be divided mentally at the point of rotation, giving us the two halves [3,4,5]
        and [1,2]. if we put put a pointer in the middle of the array, there is a chance that it is either on the "left half" or the "right half".
        comparing this middle point to the beginning of the array will tell us what half we are in
        if the middle point is greater than the beginning, we are in the left half, if it is smaller we are in the right half
        
        how does this help us? 
        there are 4 outcomes:
        1. the middle point is somewhere in-between the left half, and we need to iterate through the right half only [3,4,5,6,1,2]
        2. the middle point is right on the money, and is the exact min we are looking for [4,5,1,2,3], which would mean that it is at the beginning of the right half
        3. the middle point is in the right half of the array, but not quite at the minimum [5,1,2,3,4]
        4. the middle point is in the left half of the array, because the entire array is a left half, meaning that its been rotated 360 degrees [1,2,3,4,5]
        
        we need to use this information to eliminate one half of the array, so that we only end up with the smaller half if possible
        that would mean that in the array [3,4,5,1,2], if we started with a left pointer at 3, a right pointer at 2, and a mid pointer at 5, we need to narrow the search
        space to [1,2] meaning our left pointer has to be moved to 1. once we have the smaller half of the array, we can just take the first element of that half
        and return it
        """
        
        result = nums[0]
        leftPointer, rightPointer = 0, len(nums)-1
        
        #middlePointer = (leftPointer + rightPointer)//2 #floor division to account for odd array length giving us .5
        
        while(leftPointer <= rightPointer):
            if(nums[leftPointer] < nums[rightPointer]): # we are in the smaller half of the array, this also account for starting with outcome 4
                result = min(result, nums[leftPointer])
                break
            
            # we are not in the smaller half of the array
            middlePointer = (leftPointer+rightPointer)//2
            result = min(nums[middlePointer], result)
            if(nums[middlePointer] >= nums[leftPointer]): #outcome 1, we are in the bigger half
                #search the right half of the array
                leftPointer = middlePointer + 1
            else: # we are in the right half of the array, aka smaller half, but we don't know if we are in the middle of the half that contains our value or not
                  #so we need to search to the left. this runs when we've narrowed our search space down, and needs to exist to exit the while loop
                rightPointer = middlePointer - 1
            
        return result
