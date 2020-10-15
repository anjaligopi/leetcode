"""
Question:
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. 
Please reset to default code definition to get new method signature.
"""

import pytest
from typing import List

class Solution:
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        
        timestamps =[]
        for ele in intervals:
            timestamps.append((ele[0], "s"))
            timestamps.append((ele[1], "e"))
        
        # sort by start times
        timestamps.sort(key = lambda x : (x[0], x[1]))
        
        max_ = 0
        cnt = 0
        
        for time in timestamps:
            # add one room if a meeting starts
            if time[1] == "s":
                cnt += 1
                max_ = max(max_, cnt)
            else:
                # delete a room if a meeting ends
                cnt -= 1
                
        return max_
    
    """
            
        if len(intervals) == 0:
            return 0
        
        min_heap = []
        intervals.sort()
        # add end times to heap
        heapq.heappush(min_heap, intervals[0][1])
        
        for ele in intervals[1:]:
            if ele[0] >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, ele[1])
            
        return len(min_heap)
        
    a min-heap to store the end times of the meetings in various rooms.

So, every time we want to check if any room is free or not, 
simply check the topmost element of the min heap as that would be the room that 
would get free the earliest out of all the other rooms currently occupied.

If the room we extracted from the top of the min heap isn't free, 
then no other room is. So, we can save time here a
nd simply allocate a new room.    
    """
            
@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, ans", [ ([[0, 30],[5, 10],[15, 20]], 2) , ([[7,10],[2,4]], 1) ])
def test_min_meeting_rooms(arr, ans):
    sol1 = Solution()
    assert sol1.min_meeting_rooms(arr) == ans
