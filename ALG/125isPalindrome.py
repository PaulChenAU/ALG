# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def isPalindrome(self, s):
        if len(s) == 0 or len(s) == 1 or s is None:
            return True
        i,j = 0,len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True




if __name__ == '__main__':
    s = 'hello; WORlD'
    s2 = 'A man, a plan, a canal: Panama'
    s3 = '0P'
    s4 = '.a'
    print (s3.lower())
    a = Solution()
    print (a.isPalindrome(s3))