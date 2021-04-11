#剑指 Offer 40. 最小的k个数
#输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#Python3
class Solution(object):
    def getLeastNumbers(self, arr, k):
        #1, 使用内置sort()函数，时间复杂度O(nlogn)
        # arr.sort()
        # return arr[:k]
        #2, 大根堆,时间复杂度O（nlogk), python heapq 为小根堆，需要技术处理取负，来实现非符号部分为最大
        if k == 0: return []
        hp = [-x for x in arr[:k]] # 技术处理取负
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop()
                heapq.heappush(hp, -arr[i])
        return [-x for x in hp]
        #3, python 堆模块heapq，  nsmallest(n, iter)
        #return heapq.nsmallest(k, arr)
