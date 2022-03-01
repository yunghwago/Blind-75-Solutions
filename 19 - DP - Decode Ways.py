class Solution:
    def numDecodings(self, s: str) -> int:
        """
        when something asks you "return the amount of ways to do x" it's usually a bottom-up dynamic programming question
        
        solution: read in characters 1 by 1
        base case: if character starts with a 0 number is invalid
        
        if character is not 1 or 2, increment the output by 1
        if character is 1, increment output by 2
        if character is 2, only increment output by 2 if the next character is 0-6
        """
        
        dp = {len(s): 1} #handles base case of returning 1 on empty string and initializes our dp, set combinations of last digit alone to equal 1
        #bottom up dp solution (aka starting from the end)
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0 #0 doesn't add any additional combinations to the number, and this handles invalid numbers starting with 0
            else:
                dp[i] = dp[i+1]
            if (i +1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2] #i+2 because its a double digit number #still don't really get this part
        return dp[0]
