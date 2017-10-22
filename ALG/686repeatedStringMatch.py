# -*- coding:utf-8 -*-
# __author__=
class Solution(object):
    def repeatedStringMatch(self, A, B):
        if len(B) == 0:
            return 1
        if len(A) == 0:
            return -1
        ans,nA = 1,A
        while A.find(B) == -1:
            if len(A) > 2*len(B):
                return -1
            A = A+nA
            ans += 1
        return ans


if __name__ == '__main__':
    a = Solution()
    print (a.repeatedStringMatch("abcabcabcabc","abac"))