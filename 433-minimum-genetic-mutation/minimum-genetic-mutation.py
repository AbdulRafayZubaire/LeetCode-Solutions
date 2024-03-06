class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if not bank:
            return -1

        result = []
        visited = set()

        def diff(curr, next):
            count = sum(x != y for x, y in zip(curr, next))
            return count

        def bfs(curr, bank, count):

            if curr == endGene:
                result.append(count)
                return

            for next in bank:
                if diff(curr, next) == 1:
                    bank_copy = bank[:]
                    bank_copy.remove(next)
                    bfs(next, bank_copy, count + 1)
            return result
        bfs(startGene, bank, 0)
        return min(result) if len(result) > 0 else -1
