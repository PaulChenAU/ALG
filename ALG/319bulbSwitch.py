# -*- coding:utf-8 -*-
# __author__=''
import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))


if __name__ == '__main__':
    s = Solution()
    for i in range(1,100):
        print (i,"===> ",s.bulbSwitch(i))
    # ans = [0 for i in range(0,100)]
    # for i in range(1,100):
    #     ans[i] = s.bulbSwitch(i)
    #     # print (i,"===> ",s.bulbSwitch(i))
    # for i in range(1,100):
    #     for j in range(100):
    #         if ans[j] == i:
    #             print (j, "===> ",i)


