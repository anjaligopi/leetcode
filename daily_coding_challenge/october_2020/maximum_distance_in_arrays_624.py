import pytest
from typing import List


class Solution:
    def max_distance_brute_force(self, arrays: List[List[int]]) -> int:

        ans = float("-inf")

        for i in range(len(arrays)):
            row_ele = arrays[i]
            for j in range(i + 1, len(arrays)):
                next_row_ele = arrays[j]
                for col1 in range(len(row_ele)):
                    for col2 in range(len(next_row_ele)):
                        # print(row_ele, next_row_ele, col1, col2)
                        ans = max(ans, abs(row_ele[col1] - next_row_ele[col2]))

        return ans

@pytest.mark.parametrize("arr, ans", [ ( [[1, 2, 3], [4, 5], [1, 2, 3]] , 4), 
                                        ([[1, 2, 3], [4, 50], [-3, 1, 2]] , 53) ] )
def test_max_distance_brute_force(arr, ans):
    sol = Solution()
    assert sol.max_distance_brute_force(arr) == ans
    assert sol.max_distance_brute_force(arr) == ans


# Run using pytest daily_coding_challenge/october_2020/maximum_distance_in_arrays_624.py --maxfail=2 (exits only after two failed cases,
# this ensures that all test cases are run).
