class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)

        left_prev, current_node = dummy_head, head
        for i in range(left - 1):  # left point tak pahuchne ke lite kitne step 
            left_prev, current_node = current_node , current_node.next

        prev = None
        for i in range(right- left +1): # kitne step me left to right ka link swap karenge
            next_pointer = current_node.next
            current_node.next = prev
            prev , current_node =  current_node , next_pointer

        left_prev.next.next = current_node
        left_prev.next = prev
        return dummy_head.next