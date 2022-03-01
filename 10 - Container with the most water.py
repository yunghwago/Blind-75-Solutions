class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        thoughts
        the max height of a container can be obtained by getting the two largest values in the array, and getting the smaller of those two values
        the length of the container can be obtained by determining how many indices apart two values are
        with this information, we can perform the calculation for area, but how do we know what the optimal area is?
        
        instinct tells me to use a sliding window
        start with leftPointer at index 0, and rightPointer at index 1, and compute the area for that, we can move the right pointer as we iterate through the array, comparing
        areas computed with a max area stored, but how do we know when to move the left pointer?
        """
        """
        #brute force solution
        result = 0
        for l in range(len(height)): #left pointer iteration
            for r in range(l+1, len(height)): #right pointer iteration
                area = (r-l)*min(height[l], height[r])
                result = max(result, area)
        return result
    
        #this works in the testcase, but the time limit exceeds in the actual problem, meaning there's probably a linear solution
        """
        
        #linear time solution
        #start with left pointer all the way on the left side, and right pointer all the way on the right side, so we start with an already kind of big container
        leftPointer, rightPointer = 0, (len(height)-1)
        result = 0
        
        while(leftPointer < rightPointer):
            #compare what's to the right of the leftPointer, to what's to the left of the rightPointer. shift the pointer that is currently lower in height
            area = (rightPointer-leftPointer)*min(height[leftPointer], height[rightPointer])
            result = max(result, area)
            
            if(height[leftPointer] < height[rightPointer]): #left pointer is shorter
                leftPointer += 1
            else: #either right pointer is shorter, or they are equal. i just realized that them being equal doesn't matter, because this step (having equal heights) always 
                  #results in a loss of volume 
                rightPointer -=1
        return result
