# move Zero
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 双指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # length = len(nums)
        # i = j = 0
        # while j < length:
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #     j += 1
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if (i != j):
                    nums[i] = 0
                j += 1
