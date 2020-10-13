"""
Question:
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def find_mid(head):
            
            dummy = ListNode(None)
            dummy.next = head
            slow = dummy
            fast = dummy
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def sort_merge_halves(left, right):
            
            dummy = ListNode(None)
            curr = dummy
            
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                
                curr = curr.next
                
            if left:
                curr.next = left
            if right:
                curr.next = right
                
            return dummy.next
        
        # merge sort - bottom up
        # recursively split into halves
        # sort and merge the halves
        
        if head is None or head.next is None:
            return head
        
        mid = find_mid(head)
        second_head = mid.next
        # end the left half
        mid.next = None
        
        l = self.sortList(head)
        r = self.sortList(second_head)
        return sort_merge_halves(l, r)