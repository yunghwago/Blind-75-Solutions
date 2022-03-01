class Solution:
    def climbStairs(self, n: int) -> int:
        """
        solution is basically the fibonacci sequence
        
        let's look at a staircase of size 5
        
        to step onto the 5th step, accounting for the 0th step we have 1 combination (0th step to 5th step)
        if we include the 4th step, we add another 1 combination (0-4-5) (0-5)
        3rd step, we add 2 combinations (0-3-4-5), (0-3-5)
        for the second step, we can just sum the number of combinations for the 3rd step and 4th step. we don't need to add 2 to this sum, because we've already taken
        the first step into account (aka stepping onto the 3rd step) on the 4th step calculation, and the first 2-step into account in the 5th step calculation
        """
        dp = []
        one, two = 1, 1 #permutations starting with 1 step, permutations starting with 2 steps #two will always be the nth fibonacci sequence that comes before one's
        dp.append(1)
        dp.append(1)
        for i in range (n-1): #n-1 here because we're moving 2 steps at a time
            temp = one #store one before its been changed
            one = one + two
            dp.append(one)
            two = temp #two has to be shifted after "one" is updated, order matters a lot here for the fibonacci sequence
        print(dp)
        return one
