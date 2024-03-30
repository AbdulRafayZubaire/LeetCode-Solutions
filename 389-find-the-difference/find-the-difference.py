class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        m = {}

        for i in s:
            try:
                m[i] += 1
            except:
                m[i] = 1

        for i in t:
            try:  
               m[i] -= 1
               if m[i] == 0:
                    del m[i]
            except:
                return i