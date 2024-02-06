class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        if all(num == 1 for num in nums):
            return len(nums) - 1
        count = 0
        max_count = 0
        delete_index = -1
        for i in range(0, len(nums)):

            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                if delete_index == -1:
                    delete_index = i
                else:
                    max_count = max(count, max_count)
                    count = i - delete_index - 1
                    delete_index = i
    
        return max(count, max_count) 