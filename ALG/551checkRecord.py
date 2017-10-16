# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ca = s.count('A')
        if ca > 1:
            return False
        i,cl = 0,0
        while i < len(s):
            if s[i] == 'L':
                cl += 1
                if cl > 2:
                    return False
            else:
                cl = 0
            i += 1
        return True

if __name__ == '__main__':
    a = Solution()
    print (a.checkRecord('LALL'))