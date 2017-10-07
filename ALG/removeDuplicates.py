# -*- coding:utf-8 -*-
# __author__=''
def removeDuplicates(nums):
    if nums is None or len(nums) == 0:
        return None
    elif len(nums) == 1:
        return 1
    else:
        i = 0
        j = 1
        num = 1
        while True:
            if j == len(nums):
                break
            elif nums[i] == nums[j]:
                j += 1
            elif nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                num += 1
                j += 1
        return num




if __name__ == '__main__':
    nums = [0,1,1,1,2,3,3]
    print (removeDuplicates(nums))