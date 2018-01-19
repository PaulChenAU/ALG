# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0
        ans = []
        def jumps(loc, count):
            if loc == len(nums) - 1:
                ans.append(count)
            elif loc >= len(nums):
                return
            else:
                for i in range(1, nums[loc]+1):
                    jumps(loc+i, count+1)
        jumps(0,0)
        return min(ans)








if __name__ == '__main__':
    a = Solution()
    print(a.jump([6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]))