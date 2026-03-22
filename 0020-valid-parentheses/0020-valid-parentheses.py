class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        hashMap = {')' : '(' , '}' : '{' , ']' : '['}

        for element in s:
            if stack and (element in hashMap and stack[-1] == hashMap[element]):
                stack.pop()
            else:
                stack.append(element)

        return not stack