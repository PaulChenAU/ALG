# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        a,b = nums[:],nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                a[i] = a[i+1]
                b[i+1] = b[i]
                break
        return a == sorted(a) or b == sorted(b)

if __name__ == '__main__':
    a = Solution()
    print (a.checkPossibility([4,2,1]))
