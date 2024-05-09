class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = []
        map_t = []

        if len(s) != len(t):
            return False

        for i in s:
            map_s.append(s.index(i))
        for i in t:
            map_t.append(t.index(i))

        if map_s != map_t:
            return False
        return True