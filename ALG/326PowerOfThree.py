# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while True:
            if n == 1:
                return True
            if n % 3 == 0 and n != 0:
                n = n/3
            else:
                return False

if __name__ == '__main__':
    a = Solution()
    print (a.isPowerOfThree(0))



'''
1
3
9
27
81
1
11
1001
11011
1010001
'''