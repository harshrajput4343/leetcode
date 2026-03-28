from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # -----------------------
        # Step 1: Validate matrix
        # -----------------------
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if lcp[i][j] > 0:
                    if i + 1 < n and j + 1 < n:
                        if lcp[i][j] != 1 + lcp[i+1][j+1]:
                            return ""
                    else:
                        if lcp[i][j] != 1:
                            return ""

        # -----------------------
        # Step 2: DSU (Union-Find)
        # -----------------------
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)

        # -----------------------
        # Step 3: Assign chars
        # -----------------------
        res = ['?'] * n
        root_to_char = {}
        curr = ord('a')

        for i in range(n):
            root = find(i)
            if root not in root_to_char:
                if curr > ord('z'):
                    return ""
                root_to_char[root] = chr(curr)
                curr += 1
            res[i] = root_to_char[root]

        res = ''.join(res)

        # -----------------------
        # Step 4: Recompute LCP
        # -----------------------
        check = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if res[i] == res[j]:
                    check[i][j] = 1
                    if i + 1 < n and j + 1 < n:
                        check[i][j] += check[i+1][j+1]

        if check != lcp:
            return ""

        return res