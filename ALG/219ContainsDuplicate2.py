# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1 or nums is None:
            return False
        dic = {}
        for index,item in enumerate(nums):
            if item in dic and index - dic[item] <=k:
                return True
            dic[item] = index
        return False

if __name__ == '__main__':
    dic = {}
    r = [1,2,3,4,5,6,1,2,3]
    a = Solution()
    print (a.containsNearbyDuplicate(r,5))
