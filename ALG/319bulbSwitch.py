# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        num = 1
        count = 3
        pcount = 3
        for i in range(1,n+1):
            if pcount == 0:
                count += 2
                pcount = count
                num += 1
            pcount = pcount - 1
        return num


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


