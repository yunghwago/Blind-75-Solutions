class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        brute forcing the solution ALONE, to find every triple combination of sums here won't even work, because the array can contain duplicates, and the problem specifically
        says:
        Notice that the solution set must not contain duplicate triplets.
        
        first thought: for every number in the array, run two sum, then prune duplicates at the end of the operation
        pseudocode would look something like this:
        
        threeSums = [(0,0,0)]
        for n in nums:
            append to threeSums = twoSum(n, nums) # where n is the target
        
        removeDupes(threeSums)
        return threeSums
        """
        """
        solution: the solution above for the most part was right, but i forgot 1 important step...
        first, and this should really be a habit of mine by now the input array has to be sorted
        so the array [-3,3,4,-3,1,2] becomes [-3,-3, 1,2,3,4]
        this allows us to compare our current number to the previous number, allowing us to skip it if they are equal, removing the need to remove duplicates
        
        time complexity = O(nlogn) (sorting the array) + O(n^2) (running twoSum n times) = O(n^2)
        """
        result = [] #result will be returned as a list of lists
        nums.sort() #sort the input array
        
        for i, number in enumerate(nums): #what is the index being used for here? to check current number to previous number and see if they are the same
            if i > 0 and nums[i] == nums[i-1]: #duplicate value found
                continue
            
            #two sum II implementation
            leftPointer, rightPointer = i+1, (len(nums)-1)
            while leftPointer < rightPointer:
                currentSum = number + nums[leftPointer] + nums[rightPointer]
                if currentSum < 0:
                    leftPointer = leftPointer + 1
                elif currentSum > 0:
                    rightPointer = rightPointer -1
                else: #currentSum == 0:
                    result.append((number, nums[leftPointer], nums[rightPointer]))
                    #now we have to update our pointers
                    leftPointer += 1 #updating the leftPointer alone will be enough to update everything else when the loop is run again
                    while nums[leftPointer] == nums[leftPointer-1] and leftPointer < rightPointer: #leftPointer was updated to duplicate value
                        leftPointer += 1
        return result
