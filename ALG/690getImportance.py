# -*- coding:utf-8 -*-
# __author__=''
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        ans = 0
        que = [id]
        while len(que) != 0:
            a = que[0]
            del que[0]
            for i in employees:
                if i.id == a:
                    ans += i.importance
                    for j in i.subordinates:
                        que.append(j)
        return ans