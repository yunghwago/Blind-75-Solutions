class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #why can't we compute every single subarray for every single value
        #that would look something like this
        #for i #iterate through array
        #      for j #go through every value for every value in the array
        #            for k #compute the sum
        #which would be a time complexity of O(n^3), which is terrible
        
        #how do we make this more efficient?
        #ignore negative prefixes
        #for example: in the example [-2,1,-3,4,-1,2,1,-5,4]
        #when we are computing the max sum for -2, we start with a max sum of -2 so far
        #when we iterate through the array, and get to 1, our max sum so far is -1, but we can ignore the -2 because it makes our sum actually smaller
        #so our max sum is 1
        #now when we skip a few steps and get to 4, after having already ignored -2 completely the prefix for 4 (1+-3) will be -2, so we should ignore that completely too
        #let's skip a few more steps and get to 2, although a negative number comes before it, the prefix, with the part [-2,1,-3] already ignored adds up to 3 (4+-1),
        #so we can't ignore the -1, because that would mean ignoring the 4 too since the array has to be contiguous
        
        #how do we implement this? sort of like a sliding window
        #left pointer will start at the beginning of the array, then move to sit at the value that comes after the value we've ignored (negative prefixes)
        #right pointer will move across the array, computing the maxsum
        #maxsum will be tracked, and overwritten if needed
        #time complexity = O(n), because we only need to go through the array once
        
        maxValue = nums[0] #initialize starting max value that will be returned
        currentSum = 0
        
        for n in nums:
            if currentSum < 0:
                currentSum = 0 #reset current sum, aka we have a negative prefix and need to ignore previous numbers
            currentSum += n
            maxValue = max(maxValue, currentSum)
            
        return maxValue
