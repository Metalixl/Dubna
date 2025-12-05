import random
# n=int(input())
# a=int(input())
# b=int(input())

# def sp(a, b):
#     r = [random.randint(a, b) for i in range(n)]
#     return r

def hz(r):
    if len(r) < 2:
        return None
    ms=10000000000
    ls=0
    for j in range(len(r)-1):
        c=r[j]+r[j+1]
        if c <= ms:
            ms=c
            ls=(j, j+1)
    return ls

def testhz():
    if hz([0, 1, 2])==(0, 1):
        print('t')
    else:
        print('error')

    if hz([0, 1, 2, -2])==(2, 3):
        print('t')
    else:
        print('error')

testhz()
