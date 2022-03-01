class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #"You must write an algorithm that runs in O(n) time and without using the division operation."
        # what does this mean for us? we can't use a brute force solution (because that would run in O(n^2) time)
        # and we cant use a solution where we multiply every number together, and iterate through the array, dividing by the current number
        
        #solution: two pass solution. have an array that stores results, that we will return eventually
        #for the first pass, compute all of the prefixes of the array
        #for the example problem [1,2,3,4], this will give us a prefix array of [1,1,2,6] (first value has no prefixes, so it will use a default value of 1)
        #for the next step, we go through nums again, but this time compute all of the postfixes
        #the postfix array for [1,1,2,4] would be [24,12,4,1]
        #we could create a second array to hold these postfixes, but to save space we can just multiply what is in our prefix array by our postfix values
        
        result = [1]*(len(nums)) #create an array of size nums with all values to 1
        prefix = 1
        
        #prefix pass
        for i in range (len(nums)):
            result[i] = prefix
            prefix *= nums[i] #compute prefix after storing result in i so that we don't count the current value in the array
        
        #postfix pass
        postfix = 1
        for i in range (len(nums) -1, -1, -1): # a way of iterating through the list in reverse order in python
            #it's basically saying start with a value 1 less then len(nums), keep going until you get to just before -1, by steps of -1
            #note to self why is there a len-1 here, and not above?
            #for loops in python say that you should start AT a value, and go until the value RIGHT BEFORE the range value. 
            #so in the for loop above we are starting at 0, and going until right before len(nums), which is len(nums)-1
            #and in the for loop below, we are starting at len(nums)-1, and going until right before the negative-1st entry, which is 0 
            #so although theres a len-1 in once place and len in the other, it is the same search space 
            result[i]*= postfix
            postfix *= nums[i]
        
        return result
            
