class Solution:
    def minPartitions(self, n: str) -> int:
        maximum = 0
        for i in n :
            maximum =  max(maximum , int(i))
        return maximum




# 32 = 10 + 11 + 11 = 3 bianry deci degit required 
#pproach = find max in the given digit like in 32 , 3 is maximum . in 51 , 5 is the maximum 
#so return the max digit it would be answer 