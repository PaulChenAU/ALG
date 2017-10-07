# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        while num > 0:
            sum += num % 10
            num = int(num / 10)
            if sum >= 10:
                sum2 = 0
                while sum >0:
                    sum2 += sum % 10
                    sum = int(sum / 10)
                sum = sum2
        return sum

if __name__ == '__main__':
    a = Solution()
    print (a.addDigits(1234567891))