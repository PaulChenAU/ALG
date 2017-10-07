# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] != i:
                return i
        return nums[len(nums)-1]+1

if __name__ == '__main__':
    nums = [0,1,2,3,4]
    a = Solution()
    print (a.missingNumber(nums))