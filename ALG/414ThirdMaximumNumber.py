# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or nums is None:
            return
        nums = list(set(nums))
        nums.sort(reverse=True)
        return nums[2] if len(nums) >=3 else max(nums)


if __name__ == '__main__':
    a = Solution()
    print (a.thirdMax([1,3,2,4,5]))









'''

1 2 3 4 5

2 1 3 4 5





'''