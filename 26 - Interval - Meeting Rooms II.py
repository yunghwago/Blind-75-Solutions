class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        so we have to count the maximum amount of overlaps at any given time, and return the maximum amount of overlaps
        
        new implementation: keep track of the current meeting, and compare future meetings to it. if they overlap, increment the current amount of overlaps
        if they don't, set that as our new current meeting
        """
        """
        new new implementation
        create two arrays, one that contains all start times and one that contains all end times
        
        if a start time is under an end time, increment the current amount of meetings by 1, and move along the start time array
        if a start time is equal to, or above an end time, decrement the current amount of meetings by 1, and move along the end time array
        do this until both arrays are exhausted, and return the maximum amount of meetings held at a time
        """
        #intervals.sort(key = lambda i : i[0] ) #sort intervals by start time
        startTimes = sorted([i[0] for i in intervals]) #way to get all first parts of a list in a list and sort them
        endTimes = sorted([i[1] for i in intervals])
        currentMeetings, maxMeetings = 0, 0
        sPointer = 0
        ePointer = 0
        
        while sPointer < len(startTimes):
            if startTimes[sPointer] < endTimes[ePointer]:
                currentMeetings += 1
                sPointer +=1
            else:
                currentMeetings -=1
                ePointer +=1
            maxMeetings = max(currentMeetings, maxMeetings)
        return maxMeetings
