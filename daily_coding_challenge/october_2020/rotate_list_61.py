"""
Question:
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
"""

import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def str_to_ll(str_ : str):
        vals = str_.split("->")
        ll_nodes_lis = []
        
        for val in vals:
            if val != "None":
                ll_nodes_lis.append(ListNode(int(val)))

        for idx, node in enumerate(ll_nodes_lis):
            if node.val is not None and idx+1 < len(ll_nodes_lis):
                node.next = ll_nodes_lis[idx+1]
        return ll_nodes_lis[0]

    def ll_to_str(self):
        out_str = []
        ans_head = self
        while ans_head is not None:
            out_str.append(str(ans_head.val)+"->")
            ans_head = ans_head.next
        out_str.append("None")
        return "".join(out_str)

class Solution:
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        
        if not head or not head.next or k==0:
            return head
        
        num_nodes = 1

        curr = head

        while curr.next:
            num_nodes += 1
            curr = curr.next

        k = k % num_nodes

        if k == 0:
            return head

        tortoise = head
        hare = head

        for i in range(k):
            hare = hare.next

        while hare.next:
            hare = hare.next
            tortoise = tortoise.next

        temp = tortoise.next
        tortoise.next = None
        hare.next = head
        return temp

# Leetcode timeout is mostly 3s
@pytest.mark.timeout(3)
@pytest.mark.parametrize("inp, k, out", [("1->2->3->4->5->None", 2, "4->5->1->2->3->None")])
def test_rotate_right(inp, k, out):
    sol1 = Solution()
    ll_head = ListNode.str_to_ll(inp)
    # print([node.val for node in ll_head])
    # print(ll_head)
    inp = ll_head
    out1 = sol1.rotate_right(inp, k)
    out_str = out1.ll_to_str()
    assert  out_str == out

# pytest daily_coding_challenge/october_2020/rotate_list_61.py --maxfail=4