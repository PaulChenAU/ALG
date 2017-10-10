# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s += t
        ans = 0
        for i in range(0,len(s)):
            ans = ans ^ ord(s[i])
        return chr(ans)

if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    print (s+t)
    a = Solution()
    print (a.findTheDifference(s,t))
