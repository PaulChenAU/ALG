# -*- coding:utf-8 -*-
# __author__=''
'''

Find the Bug

unfinished find binary circle

find the bugs

'''
def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    print (d,l)
    for p in range(1, l):
        ok = True
        for i in range(l-p+1):
            print (i,i+p)
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1

if __name__ == '__main__':
    print (solution(955))