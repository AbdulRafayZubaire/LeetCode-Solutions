class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 or n== 2 or n == 3:
            return n
        a = 1
        b = 2
        c = 0
        for i in range(0, n-2):
            c = a+b
            a = b
            b = c
        return c

        