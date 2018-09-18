#!/usr/bin/python3
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        new_A = []
        for i in A:
            if i % 2 == 0:
                new_A.insert(0, i)
            else:
                new_A.append(i)
        return new_A


if __name__ == '__main__':
    b = [3, 1, 2, 4]
    a = Solution()
    print(a.sortArrayByParity(b))
