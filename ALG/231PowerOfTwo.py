# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            if n % 2 != 0:
                return False
            return self.isPowerOfTwo(n/2)

if __name__ == '__main__':
    r = [1,2,4,8,16,32,64,128,256,512,1024]
    a = Solution()
    print(a.isPowerOfTwo(8))