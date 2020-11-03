"""
Question:
Given a string s, the power of the string is the maximum length of a 
non-empty substring that contains only one unique character.

Return the power of the string.
 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
"""

import pytest

class Solution:
    def max_power(self, s: str) -> int:
        
        if not s:
            return 0
        
        count = 1
        max_count = 1
        
        if len(s) == 1:
            return max_count
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            max_count = max(count, max_count)
            
        return max_count
            
@pytest.mark.timeout(3)
@pytest.mark.parametrize(
    "str_, ans", [("leetcode", 2), ("hooraaaaaaaaaaay", 11), ("j", 1)]
)
def test_max_power(str_, ans):
    sol1 = Solution()
    assert sol1.max_power(str_) == ans

# pytest daily_coding_challenge/october_2020/consecutive_characters_1446.py --maxfail=4