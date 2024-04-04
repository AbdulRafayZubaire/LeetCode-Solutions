class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp = [0]*len(nums) + 1

        # for i in range(len(nums)):

        result = 0
        def func(nums, memo):
            if len(nums) <= 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) in memo:
                return memo[len(nums)]

            res = max(nums[0] + func(nums[2:], memo), func(nums[1:], memo))
            memo[len(nums)] = res
            return memo[len(nums)]
        return func(nums, {})
            
