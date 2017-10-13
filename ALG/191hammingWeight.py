# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is None:
            return
        return bin(n).count(('1'))