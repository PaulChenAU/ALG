# -*- coding:utf-8 -*-
# __author__=''
# candidates - list[int]
# target - int
# return list[list[int]]
class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        candidates.sort()
        mid = []
        self.backtracking(candidates,target,0,mid,ans)
        return ans

    def backtracking(self,candidates,target,index,mid,ans):
        if target < 0:
            return
        if target == 0:
            ans.append(mid)
            return
        for i in range(index,len(candidates)):
            self.backtracking(candidates,target-candidates[i],i,mid+[candidates[i]],ans)



if __name__ == '__main__':
    a = Solution()
    print (a.combinationSum([2,4,3,7],7))