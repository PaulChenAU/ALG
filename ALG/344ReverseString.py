# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

if __name__ == '__main__':
    s = 'hello'
    print (s[::-1])