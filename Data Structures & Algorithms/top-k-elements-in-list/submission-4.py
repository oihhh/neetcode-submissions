class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for i in nums:
            if i in frequency_map:
                frequency_map[i] += 1
            else:
                frequency_map[i] = 1
        top_keys = sorted(frequency_map, key=lambda x: frequency_map[x], reverse=True)[:k]
        return top_keys