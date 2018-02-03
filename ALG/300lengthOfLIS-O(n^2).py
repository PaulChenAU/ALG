# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):

    @staticmethod
    def lcs(s, r):
        c = [[0] * len(r) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(len(r)):
                if s[i] == r[j]:
                    if i == 0 or j == 0:
                        c[i][j] = 1
                    else:
                        c[i][j] = 1 + c[i - 1][j - 1]
                else:
                    c[i][j] = max(c[i - 1][j], c[i][j - 1])
        return c[len(s) - 1][len(r) - 1] if len(s) > 0 and len(r) > 0 else 0

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        s_nums = list(set(nums))
        s_nums = sorted(s_nums)
        return self.lcs(nums,s_nums)


if __name__ == '__main__':
    s = Solution()
    num = [10, 9, 2, 5, 3, 7, 101, 18]
    s_num = sorted(num)
    print (num)
    print (s_num)
    print (s.lengthOfLIS(num))
