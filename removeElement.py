#/usr/bin/python3

class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)


if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    a = Solution()
    print(a.removeElement(nums, val))
