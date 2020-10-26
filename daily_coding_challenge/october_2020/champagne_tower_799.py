"""
Question:
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, 
and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, 
any excess liquid poured will fall equally to the glass immediately to the left and right of it.  
When those glasses become full, any excess champagne will fall equally to the left and 
right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  
After two cups of champagne are poured, the two glasses on the second row are half full.  
After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  
After four cups of champagne are poured, 
the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

Example 1:

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). 
There will be no excess liquid so all the glasses under the 
top glass will remain empty.
Example 2:

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower 
(which is indexed as (0, 0)). There is one cup of excess liquid. 
The glass indexed as (1, 0) and the glass indexed as (1, 1) will 
share the excess liquid equally, and each will get half cup of champange.

"""
import pytest

class Solution:
    def champagne_tower(self, poured, query_row, query_glass):
        l = [poured]
        for _ in range(query_row):
            l_new = [0] * (len(l) + 1)
            for i in range(len(l)):
                pour = (l[i] - 1)/2
                if pour > 0:
                    l_new[i] += pour
                    l_new[i+1] += pour
            
            l = l_new
                    
        return min(1, l[query_glass])


@pytest.mark.timeout(3)
@pytest.mark.parametrize("poured, query_row, query_glass, ans", [ (2,1,1,0.5) , (1,1,1,0.0) ])
def test_champagne_tower(poured, query_row, query_glass, ans):
    sol1 = Solution()
    assert sol1.champagne_tower(poured, query_row, query_glass) == ans

# pytest daily_coding_challenge/october_2020/champagne_tower_799.py --maxfail=4 