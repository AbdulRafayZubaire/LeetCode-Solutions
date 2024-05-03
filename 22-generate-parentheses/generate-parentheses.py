class Solution:
    def generateParenthesis(self, n: int, closed = False, c1 = None, c2 = None) -> List[str]:
        if n == 0:
            return [""]

        if c1 is None:
            c1 = dict()

        if c2 is None:
            c2 = dict()
            
        if closed and n in c1:
            return c1[n]
        
        if not closed and n in c2:
            return c2[n]

        if closed:
            c1[n] = ["(" + e + ")" for e in self.generateParenthesis(n - 1, False, c1, c2)]
            return c1[n]
        else:
            res = list()
            for en in range(1, n + 1):
                part_1 = self.generateParenthesis(en, True, c1, c2)
                part_2 = self.generateParenthesis(n - en, False, c1, c2)
                for e in part_1:
                    for f in part_2:
                        res.append(e + f)
            
            c2[n] = res
            return res