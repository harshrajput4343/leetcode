# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        n = getLength(head)
        self.curr = head
        
        def build(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            
            left = build(l, mid - 1)
            
            root = TreeNode(self.curr.val)
            self.curr = self.curr.next
            
            right = build(mid + 1, r)
            
            root.left = left
            root.right = right
            
            return root
        
        return build(0, n - 1)
        