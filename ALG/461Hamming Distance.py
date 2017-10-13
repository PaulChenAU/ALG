# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x is None and y is None:
            return None
        if not x or not y:
            return bin(y).count('1') if y else bin(x).count('1')
        return bin(y^x).count('1')
if __name__ == '__main__':
    a = Solution()
    print (a.hammingDistance(0,0))

'''
not x equals x is None or s == 0


'''
