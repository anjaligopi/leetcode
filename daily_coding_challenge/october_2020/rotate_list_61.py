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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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
