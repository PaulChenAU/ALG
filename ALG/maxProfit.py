# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1 or prices is None:
            return 0
        list = []
        ansmin,loc = prices[0],-1
        for i in range(0,len(prices) - 1):
            min = prices[i+1] - prices[i]
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > min:
                    min = prices[j] - prices[i]
            list.append(min)
        ans = list[0]
        for i in range(0,len(list)):
            if list[i] > ans:
                ans = list[i]
        if ans < 0:
            return 0
        return ans


if __name__ == '__main__':
    a = Solution()
    list = [7,6,5,4,3,2,1]
    print (a.maxProfit(list))