class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        question: is there ever a time where we wouldn't want to rob every other house?
        yes
        given the array [1,7,1,1,9]
        
        sorting the array messes up which houses are near each other...
        
        would it make sense to rob starting at the most profitable house? and have that be our final solution?
        no
        ex. [1,100,101,100,1]
        
        
        """
        n = len(nums)
        if n <= 2:
            return max(nums[0], nums[-1])
        
        dp = [0 for i in range(n)] #dp stores previous work ex. dp[0] is the maximum sum of houses robbed until index 0
        #so if we have an array of houses [1,2,3,1,2]
        #                            dp = [1,2,4,4,6]
        
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, n): #for loop starting at index 2
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) #current max of houses so far is either the max dp we have so far, or the second max dp, 
                                                    #plus the house 2 houses in front of it
            
        return dp[n-1]
