# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) <= 1 or nums is None:
            return False
        nums.sort()
        tmp = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == tmp:
                return True
            else:
                tmp = nums[i]
        return False

if __name__ == '__main__':
    a = Solution()
    r = []
    t = None
    print (a.containsDuplicate(t))