# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(max("".join(list(map(str,nums))).split('0')))


if __name__ == '__main__':
    a = Solution()
    print (a.findMaxConsecutiveOnes([1,1,0,1,1,1]))
    #print (max(['11','111','0000']))