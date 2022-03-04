class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        """
        some notes
        1.
        uniquePaths(0,0) = invalid
        uniquePaths(0,1) = invalid
        uniquePaths(1,0) = invalid
        uniquePaths(1,1) = 1
        
        2. 
        if we move down or right, it's like we're in the top left of a new mxn grid
        ex. if we start on a 2,3 grid, move down, we're in the starting position of a 1,3 grid 
        
        3. uniquePaths(m, n) == uniquePaths(n, m) logically speaking
        so we can use this to our advantage in our memo
        """
        #memo = {} key = (m,n), value = num of paths
        if (m,n) in memo:
            return memo[(m,n)]
        #base cases
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        
        memo[(m,n)] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)
        return memo[(m,n)]
