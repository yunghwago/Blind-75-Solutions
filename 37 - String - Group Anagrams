class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        we can sort each word in strs, and if they are equal they are anagrams
        problems with this implementation: 
        runtime will be O(m*nlogn). where nlogn is the runtime of the sorting algorithm, and m is how many times we have to run it
        we need to keep track of the original words, before they were sorted, so we can unsort each individual word in our result before it is returned
        
        """
        """
        solution: take a word apart, and put all of its letters, and counts of each letter in a dictionary
        go to the next word, and check all of its letters and counts too. if it exists in our dictionary, group it with our previous word.
        if it doesn't, add it to our... collection of dictionaries? what data structure would we use here?
        
        repeat this process
        """
        result = defaultdict(list) # not sure how the dictionary will function yet #also, using defaultdict(list) instead of {} somehow prevents a thrown exception
        
        for string in strs: # for every string in list of strings
            count = [0] *26 # a->z 
            for char in string: # for every character in each string
                #if "a" is index 0 in count, and "z" is index 25, how do we convert the letters to match these indices?
                #you could use a dictionary, but you could also convert them to ascii, and calculate the difference
                #this works because all characters in this problem consist of lower case english characters
                count[ord(char)-ord("a")] += 1
            result[tuple(count)].append(string) #why are we converting count to a tuple? in python, lists cannot be keys in a dictionary, so this is just a workaround to that
            #why append here instead of assign a value? we can see why in the print statement. we want to append strings with the same characters to the values, instead of 
            #overwriting them
            
        #print(result)
        return result.values() #way to return just the values of a dictionary in python, without the keys
    
    #runtime = O(m*n). m = num strings, n = average length of each string
