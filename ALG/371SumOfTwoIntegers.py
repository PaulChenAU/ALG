# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        p = []
        if a < 0:
            flaga = True
        if b < 0:
            flagb = True
        for i in range(0,a):
            if flaga:
                p.append(-1)
            else:
                p.append(1)
        for i in range(0,b):
            if flagb:
                p.append(-1)
            else:
                p.append(1)
        return len(p)


if __name__ == '__main__':
    a = Solution()
    print (a.getSum(-1,0))


'''
1
11


'''