class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        implementation: append newInterval to the list of intervals, sort that list by the first number in every tuple
        then merge all intervals together
        
        merging intervals works using a two pointer solution
        first pointer always points at the last number inserted into the interval
        second pointer iterates through the array
        
        if the second pointer is within the bounds of the first interval, change the first interval's second number of the tuple
        if it is not, insert it into the output list
        """
        intervals.append(newInterval)
        
        intervals.sort(key=lambda x: x[0]) #sorting the array of tuples by first tuple
        
        output = [intervals[0]]
        
        for start, end in intervals[1:]: #python lets you refer to parts of the tuple by doing for loops
                                         #this. intervals[1:] means start at array[1] instead of array[0]
            lastEnd = output[-1][1] #second part of tuple, of most recently added interval
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd) #update the ending range of the last tuple inserted
                                                      #why do it like this? in case we have a situation
                                                      #like [1,5], [2,4]
            else:
                output.append([start,end]) #attach completely new interval if no overlap is found
        return output
