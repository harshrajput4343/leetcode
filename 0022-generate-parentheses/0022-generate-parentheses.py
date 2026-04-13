class Solution:
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(s, open_, close):
            if len(s) == 2*n:
                res.append(s)
                return
            
            if open_ < n:
                backtrack(s + "(", open_ + 1, close)
            
            if close < open_:
                backtrack(s + ")", open_, close + 1)
        
        backtrack("", 0, 0)
        return res
        