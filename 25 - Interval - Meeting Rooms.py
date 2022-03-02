class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        we could store all the meeting start times and end times in a hashmap, but how can we tell if an interval overlaps with something that is in our hashmap?
        
        """
        
        """
        ok so the hashmap is actually unnessecary amounts of work
        instead we can just sort the array by start times, and keep track of our first and second interval
        if the first number in the interval in front (our second interval) is less than the second number of our interval in the back (first interval)
        we return False.
        else we keep iterating through the array
        """
        
        intervals.sort(key = lambda i : i[0] ) #sort intervals by start time
        
        for i in range (len(intervals)-1):
            i1 = i
            i2 = i +1
            
            if intervals[i2][0] < intervals[i1][1]:
                return False
        return True 
