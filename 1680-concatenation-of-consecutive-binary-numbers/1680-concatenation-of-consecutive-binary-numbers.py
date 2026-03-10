class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 +          7
        ans = 0
        bits = 0

        for i in range( 1, n+1):
            if i & (i - 1) == 0:
                bits += 1
            ans = ((ans << bits) + i) % MOD
        return ans





# n = 3 -> 1, 2 , 3   = 01 + 10 + 11 = 11011 = 27

#when no hit the power of two it need one extra bit to represent 
# no can easily become to large so we will use modulo at each step  ( (ans << bits) + i ) % MOD
# run loop from 1 to n + 1 ie n  , if number is power of 2 increase the bits and current bit shifted to left 
#so that there will be space for new number and  do modulo