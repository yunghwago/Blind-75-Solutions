class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        first step is to remove all punctuation, spacing, and capitalization
        next step is to create two pointers for a sliding window
        set one pointer to start at the beginning of our string, and one to start at the end
        compare both pointers, if they are equal, move the left one to the right by 1, and the right to the left by 1
        if they are not equal, break the operation and return false
        
        edge case: we need to account for empty strings being true
        
        """
        
        newStr = "" #holds our string with all punctuation removed
        
        for char in s:
            if char.isalnum(): #python specific function, if character is alphanumerical
                newStr += char.lower()
        l, r = 0, (len(newStr)-1)
        
        while l < r:
            if newStr[l] != newStr[r]:
                return False
            else:
                l += 1
                r -= 1
                
        return True
