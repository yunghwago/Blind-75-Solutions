class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        #neetcode's solution, use a hashset
        #insert every value in nums into the hashset, and if it already exists before it is about to be inserted, return true
        #else return false
        
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
