# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1 or prices is None:
            return 0
        maxProfit = 0
        for i in range(0,len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                maxProfit += prices[i+1] - prices[i]
        return maxProfit