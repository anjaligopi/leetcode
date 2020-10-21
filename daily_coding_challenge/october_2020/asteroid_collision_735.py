"""
Question:

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. 
Asteroids moving the same direction never meet, so no asteroids will meet each other.
"""

from typing import List
import pytest

class Solution:
    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        
        # stack
        res = []
        
        for x in asteroids:
            
            # collision case
            while res and x < 0 and res[-1] > 0:
                # same magnitude for both asteroids
                if res[-1] + x == 0:
                    res.pop()
                    break # don't append curr value to the stack
                    
                elif abs(x) < res[-1]:
                    break
                    
                else:
                    #abs(x) > res[-1]
                    res.pop()
                    continue # keep going
                    
            else:
                res.append(x)
                
        return res


@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, ans", [ ([5,10,-5], [5,10]) , ([-2,-1,1,2], [-2,-1,1,2]) ])
def test_asteroid_collision(arr, ans):
    sol1 = Solution()
    assert sol1.asteroid_collision(arr) == ans


#pytest daily_coding_challenge/october_2020/asteroid_collision_735.py --maxfail=4 