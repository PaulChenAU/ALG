# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def trailingZeroes(self, n):
        sum = 0
        while True:
            if n < 5:
                return sum
            n = int(n/5)
            sum += n
    def jiecheng(self,x):
        sum = 1
        for i in range(1,x+1):
            sum = sum * i
        return sum

if __name__ == '__main__':
    a = Solution()
    print (a.trailingZeroes(30))
    print (a.jiecheng(30))