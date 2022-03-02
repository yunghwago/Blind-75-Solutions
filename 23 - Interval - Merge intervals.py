class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0]) #sorting the array of tuples by first digit of tuple
        output = [intervals[0]] #setting our output to the first entry of intervals prevents
                                #an edge case caused by only 1 tuple in intervals
        
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
