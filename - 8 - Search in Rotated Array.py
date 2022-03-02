class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        let's say we have an array [3,4,5,6,7,0,1,2] with a middle point of 6. when things need to be in O(log n) time, we can assume that some binary search mechanism
        is at play, which is why we have a midpoint
        
        if our target is greater than 6, then we know that we must move to the right. if 6 was somewhere on the right half of the array, we would still be moving right.
        if 6 is our biggest value, then the value doesn't exist. if 6 is at the end of the right half of the array [7,8,6], this wouldn't work, but there's no way that 
        our mid point would be there anyways
        
        what if we our target was less than 6 though? in the array [3,4,5,6,7,0,1,2], there are numbers both less than 6 on both sides of the array
        we can compare our target to the first entry in the array
        if our target is greater than the first entry in the array, but less than 6, we know that the number we are looking for must be somewhere in between the array[0]
        and 6, if our target is less than array[0], then we need to move to the right from 6
        
        
        what if we had a similar situation, but a number greater than 6 on both ends? [12, 14, 6, 8, 10]
        how would we get the algorithm to work for both less than and greater than on both halves?
        """
        
        #can we assume that the answer exists in nums? no
        
        leftPointer, rightPointer = 0, (len(nums)-1)
        
        
        while leftPointer <= rightPointer: #<= instead of <, in case we get an array of size 1
            middle = (leftPointer+ rightPointer)//2
            if nums[middle] == target:
                return middle
            #check to see which portion of the array we are in
            #are we in the left sorted portion?
            if nums[middle] >= nums[leftPointer]:
                if target > nums[middle] or target < nums[leftPointer]: #search right
                    leftPointer = middle + 1
                #elif target < nums[leftPointer]: #the array is rotated in such a way that the target is on the right side of the array
                 #   leftPointer = middle + 1
                else: #target is less than the middle, but greater than the left value, so we have to search the right side
                    rightPointer = middle - 1
            else: #we are in the right sorted portion
                if target < nums[middle] or target > nums[rightPointer]: #go left
                    rightPointer = middle - 1
                #elif target > nums[rightPointer]: #array is rotated in such a way that the large value we are looking for is on the left side of the array
                #    rightPointer = middle -1
                else:
                    leftPointer = middle + 1 
        return -1
