class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 1 if target == nums[0]or target == -nums[0] else 0


        def func(n, target, memo):
            if (len(n), target) in memo:
                return memo[(len(n), target)]
            if len(n) <= 0:
                return 1 if target == 0 else 0

            res = func(n[1:], target-n[0], memo) + func(n[1:], target+n[0], memo)
            memo[(len(n), target)] = res
            return res

        return func(nums, target, {})