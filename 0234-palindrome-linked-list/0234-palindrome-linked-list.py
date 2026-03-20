# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Step 1: Find middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Step 3: Compare first and second half
        left, right = head, prev
        while right:                      # right is shorter or equal
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True