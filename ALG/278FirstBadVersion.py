# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        for i in range(0,len(n)):
            if n[i] != i+1:
                return n[i-1]
        return n[len(n)-1]

if __name__ == '__main__':
    nums = [1,2,2]
    a = Solution()
    print (a.firstBadVersion(nums))