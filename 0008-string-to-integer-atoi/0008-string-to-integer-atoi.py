class Solution:
    def myAtoi(self, s):
        i, n = 0, len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        num = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num