# -*- coding:utf-8 -*-
# __author__=''
# n:int rtype:List[str]
'''
 一个数列 由-1和1组成,每一位数(>1)的左边的数的和都小于等于0 并且该数列总和为0



'''
def generateParenthesis(n):
    list = []
    for


if __name__ == '__main__':
    while 1:
        a = input()
        sum = 0
        for i in range(0,len(a)):
            if a[i] == '(':
                sum += -1
            elif a[i] == ')':
                sum += 1
            if sum > 0:
                print ("False")
                break
            if i == len(a) - 1:
                if sum == 0:
                    print ("True")
                else:
                    print ("False")