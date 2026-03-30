class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = defaultdict(int)
        odd = defaultdict(int)
        
        for i in range(len(s1)):
            if i % 2 == 0:
                even[s1[i]] += 1
                even[s2[i]] -= 1
            else:
                odd[s1[i]] += 1
                odd[s2[i]] -= 1
        
        return all(v == 0 for v in even.values()) and all(v == 0 for v in odd.values())