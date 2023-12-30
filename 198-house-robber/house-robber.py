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
        return self.robber(nums, {})