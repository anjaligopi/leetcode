"""
Question:
Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  
Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  
For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.


Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
"""

import pytest

class Solution:
    def bitwise_complement(self, N: int) -> int:
        
        """
        # ignore the 0b in bin(N) string
        bin_n = bin(N)[2:]
        comp_lis = []
        for ch in bin_n:
            if ch == "0":
                comp_lis.append("1")
            else:
                comp_lis.append("0")
        comp_str = "0b" + "".join(comp_lis)
        return int(comp_str, 2)
        """
        
        # xor with 1 to flip
        # use left shift and right shift
        # right shift temp so that you know you have to stop the while loop when temp becomes 0
        
        if N == 0:
            return 1
        
        bit = 1 # xor with 1
        temp = N
        
        while temp:
            N = N ^ bit
            bit = bit << 1
            temp = temp >> 1
            
        return N

@pytest.mark.parametrize("num, ans", [(0,1), (5, 2)])
def test_bitwise_complement(num, ans):
    sol1 = Solution()
    assert sol1.bitwise_complement(num) == ans

# pytest daily_coding_challenge/october_2020/complement_of_base10_int_1009.py --maxfail=4