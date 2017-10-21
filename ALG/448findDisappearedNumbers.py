# -*- coding:utf-8 -*-
# __author__='c'

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
if __name__ == '__main__':
    a = Solution()
    print (a.findDisappearedNumbers([4,3,2,7,8,2,3,1]))