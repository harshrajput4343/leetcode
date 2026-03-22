# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()   # dummy node avoids handling head separately
        
        while list1 and list2: # merge while both lists have nodes
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1

            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2: # attach remaining nodes (only one of them is non-null)
            cur.next = list1 if list1 else list2

        return dummy.next