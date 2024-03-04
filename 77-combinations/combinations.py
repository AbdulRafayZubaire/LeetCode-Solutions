class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def recursive(start, comb, result):
            if len(comb) == k:
                result.append(comb.copy())

            for i in range(start, n+1):
                comb.append(i)
                recursive(i + 1, comb, result)
                comb.pop()

            return result
        return recursive(1, [], [])