# -*- coding:utf-8 -*-
# __author__=''
def removeElement(nums, val):
    if len(nums) == 0:
        return 0
    elif val is None:
        return len(nums)
    elif len(nums) == 1:
        if nums[0] == val:
            return 0
        else:
            return 1
    elif len(nums) > 1:
        k = 0
        for i in range(0,len(nums)):
            if nums[i] == val:
                k += 1
        while k >0:
            nums.remove(val)
            k -= 1
        return len(nums)



if __name__ == '__main__':
    nums = [0,1,1,2,3,4]
    print (removeElement(nums,6))