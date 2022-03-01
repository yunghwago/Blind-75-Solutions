class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        one pass hashmap solution
        how the solution works:
        0. our goal is to iterate through the array once, avoiding the n^2 brute force solution
        1. difference between target and current number in array we are iterating through is calculated
        2. check and see if it is in our hashmap, if it is return, if not continue
        3. put current number in array in hashmap, mapped to its index
        4. return false if two sum value is not found at the end
        """
        
        hashmap = {} #dictionary that functions as our hashmap
        #hashmap will be value:index
        for i, n in enumerate(nums): #i = index, n = the current number we are looking at in nums
            diff = target - n
            if diff in hashmap: #diff was an original number found previously in the hashmap
                return [hashmap[diff], i] 
            hashmap[n] = i #insert original number into hashmap with index to pull later
        return #we're guaranteed a solution exists, so this return exists here just in case
