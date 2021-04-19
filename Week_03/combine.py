#组合
#给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 递归回溯求接
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []
        def recure(n, k, startindex):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(startindex, n-(k-len(path))+2): # n-(k-len(path))+2,这里为剪枝，去除不必要得分支
                path.append(i)
                recure(n, k, i+1)
                path.pop(-1)
        recure(n, k, 1)
        return result
