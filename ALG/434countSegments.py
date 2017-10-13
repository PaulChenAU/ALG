# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or not s:
            return 0
        i,j,ans = 0,0,0
        while i < len(s):
            if s[i] == ' ':
                j = 1
            elif i == 0:
                ans += 1
            elif s[i] != ' ':
                if j == 1:
                    ans += 1
                    j = 0
            i += 1
        return ans





if __name__ == '__main__':
    str = 'Hello, my name is John'
    str2 = '  h '
    str3 = 'h  '
    a = Solution()
    print (a.countSegments(str3))