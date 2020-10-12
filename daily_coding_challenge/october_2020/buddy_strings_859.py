"""
Question:
Given two strings A and B of lowercase letters, return true if you can swap two letters in A 
so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j 
and swapping the characters at A[i] and A[j]. For example, 
swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
"""

import pytest
from collections import Counter

class Solution:
    def buddy_strings(self, A: str, B: str) -> bool:
        
        """
        # Brute Force
        a = list(A)
        b = list(B)
        
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                temp1 = a[i]
                temp2 = a[j]
                a[i], a[j] = a[j], a[i]
                if a == b:
                    return True
                else:
                    a[i] = temp1
                    a[j] = temp2
        return False            
        """

        if len(A) != len(B): 
            return False
        
        Count_A, Count_B = Counter(A), Counter(B)
        if Count_A != Count_B: 
            return False
        
        diff_places = sum([i!=j for i,j in zip(A,B)])
        
        if diff_places not in [0, 2]: 
            return False
        
        # diff_places == 0, it means that we changed two equal symbols. 
        # We can not do it if string has different symbols, like abtlpe ie., no repeating chars
        if diff_places == 0 and len(Count_A) == len(A): 
            return False
        
        #diff_places == 2, it means that we changed two different symbols.
        # We can not do it if string is just one symbol repeated, like ddddddd
        if diff_places == 2 and len(Count_A) == 1: 
            return False
        
        return True

@pytest.mark.timeout(3)
@pytest.mark.parametrize("str_a, str_b, ans", [("aaaaaaabc", "aaaaaaacb", True) , ("", "aa", False), ("ab", "ba", True)])
def test_buddy_strings(str_a, str_b, ans):
    sol1 = Solution()
    assert sol1.buddy_strings(str_a, str_b) == ans

# pytest daily_coding_challenge/october_2020/buddy_strings_859.py --maxfail=4 