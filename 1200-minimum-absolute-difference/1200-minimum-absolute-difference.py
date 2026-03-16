class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        # find min absolute difference
        min_d = float('inf')
        for i in range(1, len(arr)):
            min_d = min(min_d, arr[i] - arr[i - 1])

        # store arr pair in result array
        result =   []

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_d :
                result.append([arr[i -1],arr[i]])

        return result