class Solution:

    def climb(self, n, memo):
        if n == 0:
            return 1
        if n < 0:
            return 0

        if n in memo:
            return memo[n]
        
        memo[n] = self.climb(n-1, memo)+self.climb(n-2, memo)

        return memo[n]
    def climbStairs(self, n: int) -> int:
        return self.climb(n, {})
        