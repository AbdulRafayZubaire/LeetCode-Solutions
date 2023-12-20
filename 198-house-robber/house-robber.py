class Solution:

    def rob_dp(self, nums, i, memo=None):
        if i < 0: return 0
        if memo is None:
            memo = {}
        if i in memo: return memo[i]

        result = max(self.rob_dp(nums, i-2, memo)+ nums[i], self.rob_dp(nums, i-1, memo))
        memo[i] = result
        return result



    def rob(self, nums: List[int]) -> int:
        return self.rob_dp(nums, len(nums)-1)

        