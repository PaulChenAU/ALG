class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k > len(nums) or len(nums) == 0:
            return
        suml = [0]
        for i in range(0,len(nums)):
            pre_sum = nums[i] + suml[-1]
            suml.append(pre_sum)
        max_sum = max(suml[i+k]-suml[i] for i in range(0,len(suml)-k))
        return float(max_sum)/float(k)

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    nums2 = [-1]
    k = 1
    a = Solution()
    print a.findMaxAverage(nums,4)
