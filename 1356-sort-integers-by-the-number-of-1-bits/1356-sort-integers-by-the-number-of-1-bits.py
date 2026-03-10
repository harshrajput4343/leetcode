class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x : (bin(x).count('1'), x))



#primary key - set bit count (no of 1 ones if same then numbers in ascending)

# 0 - 0000 -> 0 ones    0 bit - 0
#  1 - 0010 -> 1 ones   1 bit - 1,2,4,8
#  2 - 0010 -> 1 ones   2 bit - 3,5,6
#  3 - 0011 -> 2 ones   3 bit - 7
#  4 - 0100 -> 1 ones 
#  5 - 0101 -> 2 ones 
#  6 - 0110 -> 2 ones 
#  7 - 0111 -> 3 ones 
#  8 - 1000 -> 1 ones 