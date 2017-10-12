# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1 or n is None:
            return 0
        i = 1
        while n - i > i:
            n = n - i
            i += 1
        return i

if __name__ == '__main__':
    a = Solution()
    print (a.arrangeCoins(8))

