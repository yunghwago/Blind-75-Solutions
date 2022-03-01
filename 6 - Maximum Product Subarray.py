class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #like the maximum sub problem, the brute force solution (computing the product so far of every entry, with every combination) gives us a runtime of
        #O(n^2), which is terrible
        
        #how do we cut this down?

        #first thought: iterate through the array, but ignore negative numbers, because as soon as we run into a negative number the largest product will be 
        #less than what we have now, so we should store the largest product so far and start the process again from the index after that
        
        #this is not completely true. why is this the case? let's say we have an array [1, -2, -3]. although -2 is a lower product than 1, -2*-3 is 6, which is greater,
        #because two negatives make a positive. we have to account for even amounts of negatives, and somehow ignore odd amounts of negatives
        
        #solution: iterate through the array, keeping track of the maximum and minimum products as i do it
        #why keep track of the minimum product?
        #because the minimum product multiplied by a negative number that comes after it in the array, might equal the new maximum in the array, solving our problem
        #with identifying odd and even amounts of negatives
        
        #EDGE case: a 0 in the array would reset the maximums and minimums being kept track of so far, what if we have an array [-1,-2,-3,0,3,5]?
        #to solve this reset the temporary maximum and minimums to 1 when a 0 is found, so we can continue keeping track of things
        
        #value we will return
        maxReturn = max(nums)
        #set temporary maximums and minimums
        currentMax, currentMin = 1, 1
        temp = 1 #value to be compared to our maxes and mins
        
        for n in nums:
            temp = currentMax * n #for the currentMin calculation we need the currentMax value before it is changed, so it is stored here
            if(n == 0):
                currentMax, currentMin = 1, 1
                continue #continue to the next iteration of the loop
            
            currentMax = max(currentMax * n, currentMin * n, n) #why have an n here? if we have an array [-1, 8], we need to ignore the -1, because currentMax and currentMin
                                                                #will both be -1, giving us -8 which is not true. also putting 3 parameters in max is a python specific thing
                                                                #also the n helps us "reset our position". let's say we have an array [2,3,-2,4], upon encountering -2, if we
                                                                #don't reset our position, if we instead skipped -2, instead of setting currentMax to -2, when we reach 4,
                                                                #with a currentMax of 6, our result would be 6*4 = 24 which is wrong
            print(currentMax)
            currentMin = min(temp, currentMin * n, n)
            maxReturn = max(maxReturn, currentMax)
            
        return maxReturn
    
