# for binary search
import bisect

def longestConsecutive(nums: list[int]) -> int:
    # return 0 if nums is empty
    if not nums:
        return 0
    
    # hash map for O(1) contains operation
    map = {i: 0 for i in nums}
    
    # sort nums to use binary search
    nums.sort()
    
    # counters for consecutive matches
    matches = 0
    max_matches = 0
    # max key in the hash map
    max_key = max(nums)
    # iterator that will check if there are coincidences with hash map, hence we need it ( O(1) ).  
    iterator = min(map)
        
    while iterator <= max_key:
        if iterator in map:
            matches+=1
            iterator+=1               
            continue
        else:
            max_matches = matches if max_matches < matches else max_matches
            matches = 0
        if not iterator+1 in map: 
            index = bisect.bisect_right(nums, iterator + 1)  # Find insertion point
            iterator = nums[index] if index < len(nums) else None
        else:
            iterator += 1
    return max(max_matches, matches) 

"""
algorith description:
    step 1:
        Check if the list is empty, if so return 0, if not, continue to the step 2
    step 2:
        create a hash map of all elements, I need it to have an O(1) contains operation
    step 3:
        sort initial array, I need to do so to have working binary search
    step 4:
        create all variables
    step 5:
        loop logic:
            - iterator starts at a minimum value of the list, then it starts to check 
            if it's in a hash map.
            - if so, then we increment matches variable and iterator itself.
            - if not, then we update max_matches variable with a new or an old value.
            - after all of that we check if there is an iterator that is larger by one, 
            if there is an iterator, we just increment it and the loop goes from start
            if there is not such an operator, we have to find a closest largest value 
            (i.e. if we have an iterator 5 and a list of [1, 2, 3, 9, 10, 15] the 
            value we seek for is 9) and we assign this value the iterator. We have to 
            do this in order to get rid of other values. To do so we need a binary search, 
            hence we sorted the list. 
"""

