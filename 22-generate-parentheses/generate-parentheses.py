class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def append(p, count_left, count_right, result):
            if count_left == 0 and count_right == 0:
                result.append(p)
                return
            if count_left > 0:
                append(p + "(", count_left - 1, count_right, result)

            if count_right > count_left:
                append(p + ")", count_left, count_right - 1, result)

        append("", n, n, result)
        return result