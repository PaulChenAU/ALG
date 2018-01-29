# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        if n == 2 or n == 3:
            return n - 1

        if n % 3 == 0:
            return 3 ** (int(n / 3))
        elif n % 3 == 1:
            return 2 * 2 * (3 ** (int(n / 3) - 1))
        elif n % 3 == 2:
            return 2 * (3 ** (int(n / 3)))


if __name__ == '__main__':
    a = Solution()
    print(a.integerBreak(8))
    # print (a.splits(10))
