class Solution:
    def numSteps(self, s: str) -> int:
        number = int(s,2)
        count = 0
        while number > 1:
            if number % 2 == 0:
                number = number // 2
            else:
                number += 1
            count += 1
        return count
 
 


# rules: no binary me hoga then assume it in decimal and start dividing it as decimal with 2 , if odd then add 1 and then start the same process 
#each division and addition is count as one step 
# if no is even then divide 
# if no is odd then + 1 