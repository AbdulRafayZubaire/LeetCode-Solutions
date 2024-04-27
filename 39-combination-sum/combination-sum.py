class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final_res = []
        def rec(res, candidates, target, memo):
            if sum(res) > target:
                return
            if sum(res) == target:
                final_res.append(res[:])
                return
            
            for i in range(len(candidates)):
                new_res = res + [candidates[i]]  # Update res with a new candidate
                if tuple(new_res) in memo:
                    continue
                memo[tuple(new_res)] = 1
                rec(new_res, candidates[i:], target, memo)
        rec([], candidates, target, {})
        return final_res