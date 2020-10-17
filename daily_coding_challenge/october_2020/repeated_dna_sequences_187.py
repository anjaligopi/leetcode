"""
Question:
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". 
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
"""

import pytest
from typing import List

class Solution:
    def find_repeated_dna_sequences(self, s: str) -> List[str]:
        
        ans = []
        
        if len(s)<10:
            return ans
        
        l = 0
        r = 10
        
        ans_dic = {}
        
        while r <= len(s):

            ans_dic[s[l:r]] = ans_dic.get(s[l:r], 0) + 1
            l += 1
            r += 1

        return [k for k, v in ans_dic.items() if v > 1]

@pytest.mark.timeout(3)
@pytest.mark.parametrize("str_, ans", [("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC","CCCCCAAAAA"]), ("AAAAAAAAAAAAA", ["AAAAAAAAAA"])])
def test_find_repeated_dna_sequences(str_, ans):
    sol1 = Solution()
    assert sol1.find_repeated_dna_sequences(str_) == ans

#pytest daily_coding_challenge/october_2020/repeated_dna_sequences_187.py --maxfail=4 