"""
Question:

"""
from functools import lru_cache
import math
import pytest

class Solution:
    @lru_cache(None)
    def winner_square_game(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        # non zero squares -> start from 1, not 0
        for x in range(1, int(math.sqrt(n)+1)):
            if not self.winner_square_game(n - (x*x)):
                return True
            
        return False
        
@pytest.mark.timeout(3)
@pytest.mark.parametrize("n, ans", [ (1, True) , (7, False) ])
def test_winner_square_game(n, ans):
    sol1 = Solution()
    assert sol1.winner_square_game(n) == ans

# pytest daily_coding_challenge/october_2020/stone_game_iv_1510.py --maxfail=4 