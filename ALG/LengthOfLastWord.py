# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s) == 0 or s is None:
            return 0
        loc = -1
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                loc = i
                break
        nums = 0
        for i in range(loc,-1,-1):
            if s[i] != ' ':
                nums += 1
            else:
                break
        return nums

if __name__ == '__main__':
    a = Solution()
    print (a.lengthOfLastWord(" "))
