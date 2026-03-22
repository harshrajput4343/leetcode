class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #define a stack
        stack = []
        for t in tokens:   #traversing in token
            if t not in "+-*/":
                stack.append(int(t))  #stack me append kar denge int me convert kar ke
            else:
                r = stack.pop()
                l = stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == '-':
                    stack.append(l-r)
                elif t == '*':
                    stack.append(l*r)
                else:
                    stack.append(int(l/r))

        return stack.pop()