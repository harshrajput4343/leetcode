class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
          return []
        
        #step 1:Find potential candidates
        candidate1 = candidate2 = None

        count1 = count2 = 0

        for num in nums:
            if candidate1 == num:
                count1 += 1

            elif candidate2 == num:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1  #count2 is also initialized with 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1  #count2 is also initialized with 1

            else:
                count1 -=1
                count2 -=1
        
        # step 2: verify the actual count

        result = []
        if nums.count(candidate1) > len(nums)//3 :
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > len(nums)//3 :
            result.append(candidate2)

        return result

    





