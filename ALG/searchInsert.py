# -*- coding:utf-8 -*-
# __author__=''
def searchInsert(nums, target):
    if nums is None or target is None or len(nums) == 0:
        return -1
    for i in range(0,len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)




if __name__ == '__main__':
    nums = [0,1,3,5,7]
    print (searchInsert(nums,8))