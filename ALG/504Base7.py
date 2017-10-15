# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        flag = -1 if num < 0 else 1
        num = abs(num)
        ans = ""
        while num != 0:
            b = num % 7
            num = int(num / 7)
            ans = str(b) + ans
        return ans if flag == 1 else "-"+ans

if __name__ == '__main__':
    a = Solution()
    print (a.convertToBase7(-7))
    print (" "+"a")