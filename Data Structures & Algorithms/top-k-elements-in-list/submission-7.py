class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for i in nums:
            my_dict[i] = 1 + my_dict.get(i, 0)
        for key, value in my_dict.items():
            buckets[value].append(key)
        val = []
        for num in range(len(buckets) - 1, 0, -1):
            for j in buckets[num]:
                val.append(j)
                if len(val) == k:
                    return val



        
