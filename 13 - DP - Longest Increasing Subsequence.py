class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        we can't iteratively go through the array, keeping track of the current subsequence so far, because we might reset the longest subsequence so far when we dont want to
        let's say we have [2,5,3,7,101]
        if we reach 5, then look at 3 and go "oh 3 is smaller than 5", and reset currentLIS to 0, then we would ignore the 2 we have, when it's a part of our desired answer
        
        how do we solve this problem?
        
        solution: work backwards, keeping track of the LIS of every number up until that point
        given an array [1,2,4,3], we start at 3, and say that it has an LIS of 1, because it has itself alone
        we go to 4, and say that has an LIS of 1, because LIS of 4 = max(1, 1 + LIS of 3) is not a valid operation, since 3 is smaller than 4
        then we go to 2, which would have an LIS of max(1, 1 + LIS of 4, 1 + LIS of 3). LIS of 4 and 3 are both valid since they are both larger than 2, which both give us 2
        so our LIS of 2 is 2
        our LIS of 1 will be max(1, 1 + LIS of 2, 1 + LIS of 4, 1 + LIS of 3), which would give us max(1, 1 +2, 1+1, 1+1), which is 3, which is the answer we are looking for
        
        time complexity is O(n^2), because we iterate backwards through the array, but check every value in front of the number we are iterating through
        
        now how do we implement this recursion? and how do we implement the step where we check if the number ahead is smaller, causing us not to be able to add the LIS values?
        """
        
        LIS = [1] * len(nums) #LIS of every number in the array
        for i in range(len(nums)-1, -1, -1): #python specific way to iterate through the list in reverse order
            for j in range(i+1, len(nums)): #iterate forward through the array for every element we pass while going backwards
                if nums[i] < nums[j]: #j comes after i, if j is larger than i, then it is TRUE that it is an increasing subsequence
                    LIS[i] = max(LIS[i], 1 + LIS[j]) #increment the current LIS as needed as you move forward from your backwards point in the array, if it fulfills the condition
        return max(LIS)
                    
