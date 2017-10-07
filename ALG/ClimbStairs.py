# -*- coding:utf-8 -*-
# __author__=''
# n -- int  rtype -- int
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        a , b = 1 , 2
        for _ in range(2,n):
            temp = b
            b = a + b
            a = temp
        return b




if __name__ == '__main__':
    a = Solution()
    print (a.climbStairs(35))