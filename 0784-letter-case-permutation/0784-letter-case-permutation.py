class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output =  [""]  # start me vacent
        for c in s:
            tmp = []  # temp list 
            if c.isalpha(): # agar c  alphabet hoga then upper and lower 2 choice tmp me store kara denge append se 
                for o in output:
                    tmp.append(o + c.lower())
                    tmp.append(o + c.upper())

            else:
                for o in output: # alphabaet nhi hoga to sidha add kar denge tmp me
                    tmp.append(o + c)
            output = tmp   # for each c in loop  after 1 iteration ,output ko temp de denge

        return output

        # (a) [a, A] -> (1) [a1, A1] ->(b) [a1b, a1B , A1b, A1B] -> (2) [a1b2,a1B2,A1b2,A1B2]