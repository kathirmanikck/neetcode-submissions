import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        x = collections.defaultdict(int)
        for i in nums:
            x[i] += 1
            
        sorted_items = sorted(x.items(), key=lambda item: item[1], reverse=True)
        
        l = []
        for j in range(k):
            l.append(sorted_items[j][0])
            
        return l