# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(findNums) == 0 or len(nums) == 0:
            return []
        ans, list = [], []
        for i in findNums:
            for j in range(0, len(nums)):
                if nums[j] == i:
                    append_list = nums[j + 1:]
                    list.append(append_list)
                    break
        j = 0
        while j < len(findNums):
            b = len(ans)
            for k in range(len(list[j])):
                if list[j][k] > findNums[j]:
                    ans.append(list[j][k])
                    break
            a = len(ans)
            if a == b:
                ans.append(-1)
            j += 1
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.nextGreaterElement([], [1, 2, 3, 4]))
