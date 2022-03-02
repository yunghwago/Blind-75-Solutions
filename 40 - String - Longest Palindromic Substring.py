class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        """
        intuition:
        it doesn't make sense to have a left pointer at the start of the array, and a right pointer at the start, because the longest palindrome isnt necessarily in the middle
        of the string
        
        does a stack help us here? not sure
        
        brute force solution:
        have a sliding window, and compare the first and last letter, all the way down to the middle letter for every permutation of letters, storing the maxlength of a 
        palindrome, and comparing it everytime a palindrome is found. this would work, but the runtime seems horrible
        
        """
        
        """
        brain blast
        we can check a character to see if its a candidate for a palindrome, by immediately checking the characters to the left and right of it as we are iterating through the
        string for the first time.
        for example, in the string "babad", we start at "a" (we can't run the operation on b, so we'll start the for loop at 1), and see that there is a b to the left of it
        and a b to the right of it. we expand our pointers outwards, until we find that we are at the beginning of the string, so the longest palindrome is bab
        
        next we move to the middle "b", we see that it is surrounded by an "a" on both sides, so we expand our pointers, and see that left points to a "b", and right points to a
        "d". we compare our new palindrome's (aba) length to the one we've stored, and they are both 3. repeat this operation until the letter right before the end of the string
        
        woops forgot to mention we need to handle the edge case of palindromes with even amounts of letters, like cbbd
        """
        global result
        global maxLength
        result = ""
        maxLength = 0
        
        
        def palindromeCheck(l, r, result, maxLength):
            while l >= 0 and r < len(s) and s[l] == s[r]:#while left and right pointers are in bounds and equal
                if (r-l+1) > maxLength:
                    result = s[l:r+1]#set result to the palindrome, aka letters from l to r +1
                    maxLength = r-l+1
                l -= 1
                r += 1
            print(result)
        
        
        for i in range(len(s)):
            #check for odd length palindromes first
            l, r = i, i
            #check later why is an "or" here in l>=0 or r <lens giving me the whole string?
            while l >= 0 and r < len(s) and s[l] == s[r]:#while left and right pointers are in bounds and equal
                if (r-l+1) > maxLength:
                    result = s[l:r+1]#set result to the palindrome, aka letters from l to r +1
                    maxLength = r-l+1
                l -= 1
                r += 1
            #ask drew, when i call the function this stops working. idk why
            #palindromeCheck(l,r,result,maxLength)
            #check for even length palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:#while left and right pointers are in bounds and equal
                if (r-l+1) > maxLength:
                    result = s[l:r+1]#set result to the palindrome, aka letters from l to r +1
                    maxLength = r-l+1
                l -= 1
                r += 1        
        return result
