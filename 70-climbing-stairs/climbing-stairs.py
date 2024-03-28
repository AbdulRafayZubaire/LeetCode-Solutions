class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        

        def dfs(i, n, memo):

            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = dfs(i+1, n, memo) + dfs(i+2, n, memo)
            return memo[i]

        return dfs(0, n, {})
        
        