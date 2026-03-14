class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            # step 1: pop whole 1st row and add in result     eg- 1, 2, 3
            result += (matrix.pop(0))  #by default it pop the last element 
            
            # step 2: remaining row last element pop  [result -> 1 , 2, 3]
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop()) # last element of row poppped  eg- 6 , 9

            if matrix:  # [resukt -> 1,2,3,6,9]
                result += (matrix.pop()[::-1]) # last row element pop in reversed order eg 8 , 7

            if matrix and matrix[0]:
                for row in matrix[::-1]:   #important
                    result.append(row.pop(0))

        return result