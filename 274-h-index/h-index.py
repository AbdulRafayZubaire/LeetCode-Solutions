class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_value = -sys.maxsize
        citation_count = {item: 0 for item in citations}
        
        for i in range(len(citations)):
            for value in citation_count.keys():
                if citations[i] >= value:
                    citation_count[value] += 1

        for key, value in citation_count.items():
            max_value = max(min(key, value), max_value)
        return max_value