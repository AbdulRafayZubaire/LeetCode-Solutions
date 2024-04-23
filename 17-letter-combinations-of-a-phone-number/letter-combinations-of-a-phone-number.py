class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        num_dict = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        def func(i, currStr):
            nonlocal result
            if len(currStr) == len(digits):
                result.append(currStr)
                return
            for char in num_dict[int(digits[i])]:
                func(i+1, currStr+char)

        if len(digits) > 0:
            func(0, "")

        return result


