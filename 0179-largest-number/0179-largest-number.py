class Solution:
    def largestNumber(self,nums):
        nums = list(map(str,nums))

        def cmp(a,b):
            if a + b > b + a:
                return -1

            else:
                return 1

        nums.sort(key=cmp_to_key(cmp))

        res = "".join(nums)
        return "0" if res[0] == "0" else res