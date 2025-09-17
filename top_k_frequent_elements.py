from collections import Counter
import heapq
def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)
