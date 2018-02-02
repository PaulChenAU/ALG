# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = {}
        for i in nums1:
            number = nums1_set.get(i,0)
            nums1_set[i] = number+1
        nums2_set = {}
        for i in nums2:
            number = nums2_set.get(i,0)
            nums2_set[i] = number+1
        ans = []
        for i in nums1_set:
            number2 = nums2_set.get(i,0)
            number1 = nums1_set[i]
            number = number2 if number2 < number1 else number1
            for j in range(number):
                ans.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([1,2,2,1],[2,2]))

