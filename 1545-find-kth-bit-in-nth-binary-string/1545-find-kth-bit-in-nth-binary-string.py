class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1 :
            return '0'

        length = ( 1 << n ) - 1
        mid = (length + 1)//2

        if k == mid:
            return '1'

        if k  < mid:
            return self.findKthBit(n - 1, k)

        c = self.findKthBit(n - 1, length - k + 1)
        return '1' if c == '0' else '0'



# observe pattern in middle of string there is always 1 , left side previous n string ie lower one | and right side reverse of left side 
# rather than making whole recursion tree we will try to make half left side tree
# 3 cases , if k == middle then ans direcltly return 1 . if k less than mid then similar to find k,  return self.findkth(n - 1 , k) 
# last case c = self.findthekth(n - 1, length - k + 1) return , invert of left side 