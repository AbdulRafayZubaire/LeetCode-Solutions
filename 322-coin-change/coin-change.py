class Solution(object):
    def __init__(self):
        self.memo = {}
    def coinChange(self, coins, amount):
        if amount in self.memo:
            return self.memo[amount]
        if amount == 0: return 0
        if amount < 0: return -1
        mini = -1
        for coin in coins:
            retValue = self.coinChange(coins, amount-coin)
            if ((mini == -1 or mini > retValue + 1) and retValue >= 0):
                mini = retValue + 1
        self.memo[amount] = mini 
        return mini