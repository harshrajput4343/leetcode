from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list)
        
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c)-97] += 1
            mp[tuple(freq)].append(s)
        
        return list(mp.values())