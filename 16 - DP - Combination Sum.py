class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
    
        def dfs(i, curr, total): 
            #pointer that tells us what numbers are available in candidates
            #curr = our current combination of numbers we are using so far (ex. [2,2])
            #total = the sum of the numbers in curr
            if total == target:
                result.append(curr.copy()) #append curr copy because we will still be using curr recursively
                return
            elif total > target or i >= len(candidates):
                return
            else:
                curr.append(candidates[i])
                dfs(i, curr, total + candidates[i]) #call dfs on current candidate
                curr.pop()
                dfs(i+1, curr, total) #call dfs when we can no longer include current candidate
        
        dfs(0, [], 0)
        return result
