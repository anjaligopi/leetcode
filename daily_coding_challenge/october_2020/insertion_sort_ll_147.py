"""
Question:

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode 
        4 2 1 3
        
        """
        dummy = ListNode(0)
        head1 = dummy
        current = head
        while current:
            if head1 and head1.val > current.val:  #check for negative head
                head1 = dummy
            while head1.next and head1.next.val < current.val: # moving pointer until the value is lesser
                head1 = head1.next
            pre = head1.next    #swapping the current pointer with new node pointer
            head1.next = current
            current = current.next
            head1.next.next = pre #setting last node of new list as None
        return dummy.next