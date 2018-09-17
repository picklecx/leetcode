#!/usr/bin/python3
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        i = 0
        for j in J:
        	for k in S:
        		if j==k:
        			i = i+1
        return i

if __name__=='__main__':
	a = Solution()
	a.numJewelsInStones("aA", "aAAAAbb")
