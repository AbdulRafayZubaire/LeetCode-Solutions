class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        map1 = []
        map2 = []
        s = s.split(" ")

        for i in pattern:
            map1.append(pattern.index(i))
        for i in s:
            map2.append(s.index(i))
        return True if map1 == map2 else False