class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        first impression solution:
        iterate through the array, keeping track of the substring we are on so far, its length, and the maximum length we have found so far
        if a duplicate character is found, reset the substring, add the character we are currently on to the set, and set the currentsubstr length to 1 and repeat the process
        
        this doesn't work
        why?
        "dvdf"
        
        upon reaching the second d, it resets, giving us a substring of d with length 1, goes to f and outputs df with a length of 2, when the answer is vdf with a length of 3
        """
        """
        solution: using a set to keep track of characters is in fact an efficient solution! nice
        the problem was the way we were iterating through the array. if we use a sliding window instead, we can take care of all the "inbetween" substrings
        
        now there is a problem that we have to keep in mind though:
        when we encounter a duplicate letter, like the second b in the string abcabcbb", when we get to the third "b", when we remove the first "b" from our set, 
        we also need to remove "a" from our set, because
        the longest substring has to be contiguous
        """
        
        charSet = set() # set to keep track of all characters currently in our current substring
        l = 0 #left pointer of sliding window
        result = 0
        
        for r in range(len(s)): #right pointer of sliding window will move along string, so its here in the for loop
            #when we encounter a duplicate character we need to update our set
            while s[r] in charSet: #while loop lets us remove characters that come before the duplicate character, fulfilling the contiguous string requirement
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r-l +1) #r -l + 1 is our current window size
        return result
