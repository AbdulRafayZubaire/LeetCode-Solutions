class Solution:
    def robber(self, nums, memo):
        if len(nums) <= 0:
            return 0

        if tuple(nums) in memo:
            return memo[tuple(nums)]

        result = max(nums[0] + self.robber(nums[2:], memo), self.robber(nums[1:], memo))
        memo[tuple(nums)] = result
        return result

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        count1 = self.robber(nums[1: n], {})
        count2 = self.robber(nums[0: n-1], {})
        
        
        return max(count1, count2)