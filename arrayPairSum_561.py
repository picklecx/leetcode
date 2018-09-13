#!/usr/bin/python3
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        nums.sort()
        new_nums = len(nums)
        for i in range(0, new_nums, 2):
            a = nums[i]+a
        return a


if __name__ == '__main__':
    a = Solution()
    print(a.arrayPairSum([1, 3, 2, 4]))
