# -*- coding:utf-8 -*-
# __author__=''
def searchRange(nums, target):
    list = []
    if len(nums) == 0:
        for i in range(0,2):
            list.append(-1)
        return list
    left = 0
    right = len(nums) - 1
    mid = (left + right) / 2
    mid = int(mid)
    index = -1
    while left <= right:
        if nums[mid] == target:
            index = mid
            break
        elif nums[mid] > target:
            right = mid - 1
            mid = (left + right)/2
        else:
            left = mid + 1
            mid = (left + right) / 2
    if index == -1:
        for i in range(0,2):
            list.append(-1)
        return list
    if index == 0:
        list.append(0)
        p = nums[index]
        while index < len(nums) and index >= 0 :
            if nums[index] == p:
                index += 1
                if index >= len(nums):
                    break
            else:
                print("2")
                break
        list.append(index - 1)
        return list
    p = nums[index]
    index2 = index
    while index < len(nums) and index >= 0:
        if nums[index] == p:
            index = index - 1
            if index < 0:
                break
        else:
            break
    list.append(index + 1)
    while index2 < len(nums) and index2 >= 0:
        if nums[index2] == p:
            index2 = index2 + 1
            if index2 >= len(nums):
                break
        else:
            break
    list.append(index2 - 1)
    return list



if __name__ == '__main__':
    '''
    newnums = []
    k = input()
    for i in range(0,int(k)):
        l = input()
        newnums.append(int(l))
    '''
    nums = [1,2,4,8,8,8,9]
    nums2 = [1]
    print(searchRange(nums2,1))