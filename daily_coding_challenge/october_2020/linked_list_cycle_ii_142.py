"""
Question:

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        # xn point
        def xn_point(head):

            fast = head
            slow = head
            
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return fast
                
            return None
        
        # meeting point
        p1 = xn_point(head)
        if p1 is None:
            return None
        p2 = head
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1
