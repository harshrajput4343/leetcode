class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()   # sort children greed
        s.sort()   # sort cookies size

        child = 0
        cookie = 0
        content = 0

        while child < len(g) and cookie < len(s):

            # if cookie can satisfy child
            if s[cookie] >= g[child]:
                content += 1      # child becomes content
                child += 1        # move to next child
                cookie += 1       # cookie used
            else:
                cookie += 1       # cookie too small, try next cookie

        return content