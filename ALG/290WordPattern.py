# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) == 0:
            if len(str) == 0:
                return True
            return False
        stra = str.split(' ')
        if len(pattern) == 1:
            if len(stra) == 1:
                return True
            return False
        if len(stra) != len(pattern):
            return False
        for i in range(0,len(pattern)):
            for j in range(0,len(pattern)):
                if pattern[i] == pattern[j] and i != j:
                    if stra[i] != stra[j]:
                        return False
                if pattern[i] != pattern[j]:
                    if stra[i] == stra[j]:
                        return False
        return True

if __name__ == '__main__':
    a = Solution()
    print (a.wordPattern('jquery','jquery'))