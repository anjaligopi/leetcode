"""
Question:
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""

from collections import Counter
import pytest

class Solution:
    def remove_duplicate_letters(self, s: str) -> str:
        """
        idx_dic = {s[i]:i for i in range(len(s))}
        stack = []
        
        for i in range(len(s)):
            if s[i] in stack:
                continue
            while stack and s[i] < stack[-1] and i < idx_dic[stack[-1]]:
                stack.pop()
            stack.append(s[i])
            
        return "".join(stack)
        """
    
        counts_dic = Counter(s)
        stack = []
        
        for ch in s:
            counts_dic[ch] -= 1
            if ch in stack: 
                continue
            while stack and stack[-1] > ch and counts_dic[stack[-1]] > 0: 
                # Pop all the characters in stack until they have more duplicates 
                # and less than the given charater
                stack.pop()
            stack.append(ch)
            
        return ''.join(stack)

@pytest.mark.timeout(3)
@pytest.mark.parametrize("s, ans", [("bcabc", "abc") , ("cbacdcbc", "acdb")])
def test_remove_duplicate_letters(s, ans):
    sol1 = Solution()
    assert sol1.remove_duplicate_letters(s) == ans

# pytest daily_coding_challenge/october_2020/remove_duplicate_letters_316.py --maxfail=4