class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        result = []
        
        l =len(matrix)
        for i in range(len(matrix[0])):
            row = []
            for j in range(l):
                row.append(matrix[j][i])
            result.append(row)

        return result