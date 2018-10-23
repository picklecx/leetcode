#/usr/bin/python3
"""
思路：不是移动 0，而是遇到不是 0 的数 交换到num[j]的位置上去，
然后 j += 1

"""
class Solution:
    def moveZeroes(self,nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums


if __name__ == '__main__':
    a = [0,0,1]
    c = [0,1,0,3,12]
    b = Solution()
    print(b.moveZeroes(a))
#    print(a)
    print(b.moveZeroes(c))
#    print(c)
