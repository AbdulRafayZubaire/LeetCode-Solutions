class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sys.maxsize
        curr_max = 0
        for i in range(0, len(prices)-1):
            buy = min(buy, prices[i])
            curr_max = max(curr_max, prices[i+1] - buy)

        return curr_max