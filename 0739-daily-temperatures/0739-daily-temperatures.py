class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n 
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index  = stack.pop()
                ans[prev_index] = i - prev_index  # compute day differernce 
            stack.append(i)

        return ans 



# USE Monotonic stack
# next greater next warmer next larger future greater element ---> Monotonic Stack
# ans = [0] * n --->  agar warmer day nahi mila to answer already correct hai --->  [0,0,0,0,0,0,0,0]
# Stack me temperature nahi, index store karte hain --->  days waited = current_index - previous_index
# Array ko left se right traverse karo ,--->kya aaj ka temperature stack ke top wale day se zyada hai? --> while stack and temperatures[i] > temperatures[stack[-1]]:
# aaj ka temperature previous day se zyada hai --->  Previous day ko stack se remove karo:   -->  prev_index  = stack.pop()
# Answer calculate karo: ->  ans[prev_index] = i - prev_index
# Phir current day ko stack me push karo:  ->   stack.append(i)
# reyrn ans 