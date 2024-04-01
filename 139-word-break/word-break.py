class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}
        def dfs(s, wordSet):
            if not s:
                return True
            if s in memo:
                return memo[s]
            for word in wordSet:
                if s.startswith(word):
                    if dfs(s[len(word):], wordSet):
                        memo[s]=True
                        return True
            memo[s] = False
            return False

        return dfs(s, wordDict)