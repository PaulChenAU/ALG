# -*- coding:utf-8 -*-
# __author__=''
import operator
class Solution(object):
    def combinationSum2(self, candidates, target):
        ans = []
        candidates.sort()
        mid = []
        self.backtracking(candidates,target,0,mid,ans)
        return ans
    def backtracking(self,candidates,target,index,mid,ans):
        if target < 0:
            return
        if target == 0:
            for each in ans:
                if operator.eq(each,mid):
                    return
            ans.append(mid)
            return
        if index >= len(candidates):
            return
        for i in range(index,len(candidates)):
            self.backtracking(candidates,target-candidates[i],i+1,mid+[candidates[i]],ans)

if __name__ == '__main__':
    a = Solution()
    print (a.combinationSum2([4,4,2,1,4,2,2,1,3],6))