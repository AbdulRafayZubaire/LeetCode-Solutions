class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        char_index = {}
        n = len(s)
        flag = False
        maxim = 0

        for i in range(n):
            char = s[i]
            if char in char_index:
                flag = True
                distance = i - char_index[char] - 1
                maxim = max(maxim, distance)
            else:
                char_index[char] = i

        return -1 if not flag else maxim
