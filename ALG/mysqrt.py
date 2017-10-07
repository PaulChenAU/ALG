# -*- coding:utf-8 -*-
# __author__=''
import math
class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        left = 1
        right = x
        mid = (left + right)/2
        while left <= right:
            midplus = mid + 1
            if mid * mid <= x and midplus * midplus >x:
                return mid
            elif mid * mid >=x:
                right = mid - 1
                mid = int((left + right)/2)
            else:
                left = mid + 1
                mid = int((left + right)/2)

if __name__ == '__main__':
    print (math.sqrt(5))
    a = Solution()
    print (a.mySqrt(9))