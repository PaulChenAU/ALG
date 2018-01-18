# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))


if __name__ == '__main__':
    a = Solution()
    print (a.multiply("0","0"))