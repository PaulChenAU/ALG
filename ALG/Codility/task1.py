# -*- coding:utf-8 -*-
# __author__=''
'''
Parking fee


'''
def solution(E, L):
    # write your code in Python 2.7
    if E is None or L is None or len(E)==0 or len(L)==0:
        return
    Eh = E[0:2]
    Em = E[3:5]
    Lh = L[0:2]
    Lm = L[3:5]
    en,first,next= 2,3,4
    h = int(Lh)-int(Eh)
    m = int(Lm)-int(Em)
    if h <= 0 and m <= 0:
        return
    elif h == 0 and m <= 0:
        return
    elif (h == 0 and m > 0) or (h==1 and m<=0):
        return en+first
    k = 0
    if m > 0:
        k = 1
    return en+first+(h-1+k)*next


if __name__ == '__main__':
    print (solution('10:00','11:01'))


