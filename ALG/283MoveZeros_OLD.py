# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 1:
            for i in range(0,len(nums)-1):
                if nums[i] == 0:
                    for j in range(i+1,len(nums)):
                        if nums[j] != 0:
                            tmp = nums[j]
                            nums[j] = nums[i]
                            nums[i] = tmp
                            break

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    a = Solution()
    a.moveZeroes(nums)
    print (nums)
