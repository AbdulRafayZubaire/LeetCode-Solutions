class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        cost = 0;
        n = len(colors);

        for i in range(1, n):
            if(colors[i]==colors[i-1]):
                cost += min(neededTime[i],neededTime[i-1]);
                if(neededTime[i]<neededTime[i-1]):
                    neededTime[i] = neededTime[i-1];

        return cost;