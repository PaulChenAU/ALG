# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sets = ['a','e','i','o','u','A','E','I','O','U']
        if s is None or len(s) == 0:
            return s
        left,right = 0,len(s)-1
        while left<right:
            if s[left] in sets and s[right] in sets:
                tmp = s[left]
                s = s[:left]+s[right]+s[left+1:]
                s = s[:right] + tmp + s[right+1:]
                left += 1
                right -= 1
            elif s[left] in sets:
                right -= 1
            elif s[right] in sets:
                left += 1
            else:
                right -= 1
                left += 1
        return s


if __name__ == '__main__':
    a = Solution()
    print (a.reverseVowels('leetcode'))