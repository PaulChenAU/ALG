# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) >= len(needle) and len(needle) == 0:
            return 0
        i, j , flag = 0, 0, 0
        while i < len(haystack):
            if flag == 0:
                cur = i
            if j < len(needle):
                if haystack[i] == needle[j]:
                    j += 1
                    flag = 1
                    if j == len(needle):
                        return i-j+1
                else:
                    flag = 0
                    j = 0
                    i = cur
            i += 1
        return -1




if __name__ == '__main__':
    a = Solution()
    print (a.strStr("mississippi", "issip"))
