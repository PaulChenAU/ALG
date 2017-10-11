# -*- coding:utf-8 -*-
# __author__=''
'''

password String

'''
def solution(S):
    # write your code in Python 2.7
    if len(S) == 0 or S is None:
        return -1
    maxL = []
    i,j,k= 0,0,0
    while i < len(S):
        if S[i] <= 'Z' and S[i] >= 'A':
            k = 1
        if S[i] <= '9' and S[i] >= '0':
            if j != 0 and k != 0:
                maxL.append(j)
            j = 0
            k = 0
        else:
            j += 1
            if i == len(S)-1 and k != 0:
                maxL.append(j)
        i += 1
    return max(maxL) if len(maxL) != 0 else -1



if __name__ == '__main__':
    s = "B0bBB0"
    print (solution(s))





'''
至少1个大写 没有数字
'''