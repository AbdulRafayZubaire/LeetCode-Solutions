class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        que = deque()
        count = 0
        max_count = 0

        if k == 0:
            for num in nums:
                if num == 1:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    count = 0

            return max_count
            
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0 and k > 0:
                k -= 1
                count += 1
                que.append(i)
            else:
                max_count = max(max_count, count)
                count += 1
                count = i - que.popleft()
                que.append(i)

        return max(count, max_count)