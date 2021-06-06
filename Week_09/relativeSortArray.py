#1122. 数组的相对排序

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #自定义排序
        # def _cmp(x):
        #     return (0, rank[x]) if x in rank else (1, x)

        # rank = {x: i for i, x in enumerate(arr2)}
        # arr1.sort(key=_cmp)
        # return arr1
        #计数排序
        maxlen = max(arr1)
        freq = [0] * (maxlen + 1)
        for x in arr1:
            freq[x] += 1
        res = []
        for x in arr2:
            res.extend([x] * freq[x])
            freq[x] = 0
        for x in range(maxlen + 1):
            if freq[x] > 0:
                res.extend([x] * freq[x])
        return res
