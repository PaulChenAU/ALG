# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False
        l = 1
        for i in range(1,len(s)):
            if len(s) % l != 0:
                l += 1
                continue
            pre = s[0:l]
            o = s.split(pre)
            if len(set(o)) == 1:
                return True
            l += 1
        return False


if __name__ == '__main__':
    a = Solution()
    print (a.repeatedSubstringPattern("abaababaa"))
