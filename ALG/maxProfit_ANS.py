# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0 or len(prices) == 1:
            return 0
        min,maxpro = prices[0],0
        for i in range(0,len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > maxpro:
                maxpro = prices[i] - min
        return maxpro

if __name__ == '__main__':
    a = Solution()
    list = [2,4,1]
    print (a.maxProfit(list))