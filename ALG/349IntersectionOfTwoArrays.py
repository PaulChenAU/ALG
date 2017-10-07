# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        r = []
        for l in nums1:
            if l in nums2:
                r.append(l)
        return r

if __name__ == '__main__':
    a = Solution()
    print (a.intersection([1,2,3,4],['a',1,2,'b']))