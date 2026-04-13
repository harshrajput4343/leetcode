class Solution:
    def countAndSay(self, n):
        res = "1"
        
        for _ in range(n-1):
            curr = ""
            i = 0
            while i < len(res):
                j = i
                while j < len(res) and res[j] == res[i]:
                    j += 1
                curr += str(j - i) + res[i]
                i = j
            res = curr
        
        return res
        