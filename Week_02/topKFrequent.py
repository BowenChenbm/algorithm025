#347. 前 K 个高频元素
#给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小
class Solution:
    def topKFrequent(self, nums: List[int, k: int -> List[int]:
        #1,python collections.Counter(arr).most_common(n), 时间复杂度O(nlogn)
        #return [x[0] for x in Counter(nums).most_common(k)]
        #2, 小顶堆
        count = collections.Counter(nums)
        hp = []
        for key, val in count.items():
            heapq.heappush(hp, (val, key))
            if len(hp) > k:
                heapq.heappop(hp)
        return [x[1] for x in hp]
        #
