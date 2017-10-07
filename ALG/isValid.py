# -*- coding:utf-8 -*-
# __author__=''
'''
    Leetcode 20. Valid Parentheses
    用栈做会AC且不超时 用List、数组会超时
    就用List模拟栈来做比较好

'''
def isValid(s):
    if len(s) == 1 or len(s) == 0 or s is None:
        return False
    stack = []
    flag = 0
    num = -1
    flag = 1
    for i in range(0,len(s)):
        if s[i] == '}':
            if num < 0:
                return False
            if stack[num] == '{':
                stack.pop()
                num -= 1
                continue
            else:
                return False
        if s[i] == ')':
            if num < 0:
                return False
            if stack[num] == '(':
                stack.pop()
                num -= 1
                continue
            else:
                return False
        if s[i] == ']':
            if num < 0:
                return False
            if stack[num] == '[':
                stack.pop()
                num -= 1
                continue
            else:
                return False
        stack.append(s[i])
        num += 1
        print (stack,num,i)
    if len(stack) == 0:
        return True
    return False





if __name__ == '__main__':
    s = "{}((([])))"
    print (isValid(s))