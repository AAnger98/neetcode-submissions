import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        l = []
        for n in nums:
            m[n] = m.get(n, 0) + 1
        heap = [(-freq, num) for num, freq in m.items()]
        heapq.heapify(heap)
        for i in range(k):
            freq, num = heapq.heappop(heap)
            l.append(num)
        return l