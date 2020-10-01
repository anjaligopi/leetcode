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

        """
        Linear time and constant memory algorithm

        We need to find first two minimum and first two maximum numbers to solve this problem. In addition, 
        we also need the indices to 
        which these minimum and maximum numbers belong to. 
        Once we have this information, we can check all the four possible pairs while discounting the ones 
        where min and max belong to the same index.
        There is another simpler method - initialize the min and max as the first and last element of the first array.
        Now iterate from element 1 to end of array and test for a solution using min and last element and max 
        and first element. Then update min and max.
        
        Time is O(N) and Space is O(1).
        """
    def max_distance(self, arrays: List[List[int]]) -> int:

        # since sorted, first ele in evry array is the min, last ele is the max
        # we can consider only the extreme points in the arrays to do the distance calculations.
        minn, maxn = arrays[0][0], arrays[0][-1]
        result = float('-inf')
        
        for i in range(1, len(arrays)):
            
            result = max(result, abs(minn-arrays[i][-1]))
            result = max(result, abs(maxn-arrays[i][0]))
            minn, maxn = min(arrays[i][0], minn), max(arrays[i][-1], maxn)
        
        return result


@pytest.mark.parametrize("arr, ans", [ ( [[1, 2, 3], [4, 5], [1, 2, 3]] , 5), 
                                        ([[1, 2, 3], [4, 50], [-3, 1, 2]] , 53) ] )
def test_max_distance_brute_force(arr, ans):
    # Brute Force
    sol1 = Solution()
    assert sol1.max_distance_brute_force(arr) == ans


@pytest.mark.parametrize("arr, ans", [ ( [[1, 2, 3], [4, 5], [1, 2, 3]] , 5), 
                                        ([[1, 2, 3], [4, 50], [-3, 1, 2]] , 53) ] )
def test_max_distance(arr, ans):
    # Optimized - O(N) time and O(1) space
    sol2 = Solution()
    assert sol2.max_distance(arr) == ans

# Run using pytest daily_coding_challenge/october_2020/maximum_distance_in_arrays_624.py --maxfail=3 
# (exits only after two failed cases,
# this ensures that all test cases are run).
# 1 more than the num of failing cases for everything to run :)
