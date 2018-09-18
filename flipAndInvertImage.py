#!/usr/bin/python3
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        
        new_A = []
        new_B = []
        for i in A:
            for k in range(len(i)):
                new_B.append(i[k])
            print(new_B)
        """
        for i in A:
        	i.reverse()
        for j in A:
            for k in range(len(j)):
                if j[k] == 0:
                    j[k] = 1
                else:
                    j[k] = 0
        return A
		

if __name__ == '__main__':
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    a = Solution()
    print(a.flipAndInvertImage(A))
