class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        answer = 0 
        running_sum = 0
        
        sum_count = {0:1}

        for num in nums:
            running_sum += num

            needed_sum = running_sum - goal 
            if needed_sum in sum_count:
                answer += sum_count[needed_sum]

            sum_count[running_sum] = sum_count.get(running_sum,0) + 1

        return answer