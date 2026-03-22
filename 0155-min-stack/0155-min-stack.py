class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        #Determine the new minimum value 
        if not self.stack:
            current_min = val # if the stack is empty ,new element is new min
        else:
            current_min = min(val,self.stack[-1][1])

        self.stack.append((val,current_min))
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()