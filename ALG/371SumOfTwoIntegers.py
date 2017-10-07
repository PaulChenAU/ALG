# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        '''
        ---------Right solution but TLE----------
        --Then I write this method in C and ACC--
        if a == -b:
            return 0
        while b:
            tmp = a ^ b
            b = (a & b) << 1
            a = tmp
        return a
        '''


if __name__ == '__main__':
    a = Solution()
    print (a.getSum(1,3))



'''
001
011

001
010
010
010

001
111



100
001

'''