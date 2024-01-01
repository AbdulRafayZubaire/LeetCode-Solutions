class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        result = sys.maxsize
        current_sum = 0

        while r < len(nums):
            current_sum += nums[r]
            r += 1

            while current_sum >= target:
                result = min(result, r - l)
                current_sum -= nums[l]
                l += 1

        return 0 if result == sys.maxsize else result