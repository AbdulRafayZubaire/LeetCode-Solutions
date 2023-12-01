class Solution:
    def setChild(self, nums, q, i, j):
        if i+1 < len(nums) and len(nums[i+1]) >j and (i+1, j) not in q:
            q.append((i+1, j))
        if j+1 < len(nums[i]) and (i, j+1) not in q:
            q.append((i, j+1))

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []
        q=[]
        q.append((0,0))

        while q:
            x,y = q.pop(0)
            self.setChild(nums, q, x, y)
            result.append(nums[x][y])

        return result
        