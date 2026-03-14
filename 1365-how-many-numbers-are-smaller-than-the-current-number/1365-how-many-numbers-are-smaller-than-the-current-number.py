class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums) # so that it will easy to place no acc to its superiority eg-[1,2,2,3,8]
        #                                                                     index-      0,1,2,3,4
        d = {} 
        
        for i , num in enumerate(temp):
            if num not in d:
                d[num] = i  # {1:0,2:1,3:3,8:4}
        
        res = []
        for number in nums:
            res.append(d[number]) # nums element ka value d se dekh kar res me store kara denge

        return res
