class Solution:
    def isValid(self, s: str) -> bool:
        """
        instinct:copy s to a temp variable
        left and right pointer sliding window, placed on temp
        have left pointer at an open parenthesis, and slide right pointer to the right until the appropriate closing parenthesis is found
        if the appropriate closing parenthesis is found, remove both of them from temp
        if a. the left pointer is ever at an open parenthesis
        b. the right pointer has gone through the entire string without finding a pair
        or c. temp is not completely deleted by the time we are done with our process
        return false
        else return true
        
        what is an efficient way to find what type of parenthesis the left pointer is pointing at, and check if the right pointer matches it?
        dictionary?
        
        wait this solution doesn't work
        why? 
        
        ([)]
        my solution would say that this is a valid input, because () gets removed first, giving us []
        and then [] gets removed, returning True, but that is not correct because order of parenthesis matters
        damn 
        """
        """
        okay so whats the solution?
        we can maintain the parenthesis that we have in a stack, because we should always be able to pop a parenthesis on one of the edges of the string, regardless of
        where the other matching parenthesis is to be valid. the stack being empty, can be our condition to return True
        
        we can also use a hashmap to keep track of what parenthesis match what
        """
        
        parenthesis = {
            ")" : "(", #why are we doing ")" : "(", instead of "(" : ")"? we are checking for an open parenthesis once a closing one is found on top of the stack, so this makes
            #it easier
            "}" : "{",
            "]" : "["
        }
        stack = [] #stack implemented as a list
        for char in s:
            if char in parenthesis:
                #what to do when you are inserting a closing parenthesis in the stack
                #check and see if the appropriate open parenthesis is in the stack
                if stack and stack[-1] == parenthesis[char]: #if stack = if stack is not empty (we cant start with a closing parenthesis)
                    #stack [-1] = python's way of saying last value we added to the stack. we're checking to see if that's the matching parenthesis                    
                    stack.pop()
                else:
                    return False
            else: #character is not a key in our dictionary, aka we have an open parenthesis
                stack.append(char)
        return True if not stack else False #return True if stack is empty
