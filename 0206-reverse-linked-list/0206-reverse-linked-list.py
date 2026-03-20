# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while (curr != None):
            # next_pointer initialize karenge
            next_pointer = curr.next

            #update link direction
            curr.next = prev

            #update curr and prev
            prev = curr
            curr = next_pointer

        self.head = prev
        return prev