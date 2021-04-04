# merge two sorted array
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 暴力: 合并后排序nums1[:] = sorted(nums1[:m] + nums2)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 双指针1, 从前往后
        # nums1Copy = nums1[:m]
        # nums1[:] = []
        # i = 0
        # j = 0
        # while i < m and j < n:
        #     if nums1Copy[i] < nums2[j]:
        #         nums1.append(nums1Copy[i])
        #         i += 1
        #     else:
        #         nums1.append(nums2[j])
        #         j += 1
        # if i < m: nums1[i+j:] = nums1Copy[i:]
        # if j < n: nums1[i+j:] = nums2[j:]
        
        #双指针2，从后往前，节约临时空间数组
        p1 = m - 1
        p2 = n - 1
        end_p = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[end_p] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[end_p] = nums1[p1]
                p1 -= 1
            elif nums1[p1] <= nums2[p2]:
                nums1[end_p] = nums2[p2]
                p2 -= 1
            else:
                nums1[end_p] = nums1[p1]
                p1 -= 1
            end_p -= 1

