class Solution(object):
    def __init__(self):
        self.memo = {}

    def coin(self, coins, amount):
        if amount in self.memo:
            return self.memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        mini = sys.maxsize
        for coin in coins:
            result = self.coin(coins, amount - coin)
            if result != -1 and result < mini:
                mini = result + 1

        self.memo[amount] = -1 if mini == sys.maxsize else mini
        return self.memo[amount]

    def coinChange(self, coins, amount):
        return self.coin(coins, amount)


# Example usage:
sol = Solution()
coins = [1, 2, 5]
amount = 11
result = sol.coinChange(coins, amount)
print(result)
