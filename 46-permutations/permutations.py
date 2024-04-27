class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final_result = []
        def rec(res, arr):
            if not arr:
                final_result.append(res[:])
                return
            
            for i in range(len(arr)):
                copy_arr = copy.deepcopy(arr)
                new_res = res[:] 
                new_res.append(copy_arr.pop(i))
                rec(new_res, copy_arr)
                
        rec([], nums)
        return final_result
        