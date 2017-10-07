# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1:
            return True
        for i in range(1,):
            if num == i * i:
                return True
        return False



if __name__ == '__main__':
    a = Solution()
    #print (a.isPerfectSquare(2147483648))
    print (2147444*2147444)
'''
0
1
10
100
1001
10000
11001
100100
'''