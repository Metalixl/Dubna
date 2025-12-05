a=[8, 3, 4, 7, 1]

def puz(a):
    s = 0
    x = 0
    for i in a:
        for j in range(len(a)-1, 0, -1):
            if a[j] < a[j-1]:
                s += 1
                (a[j], a[j-1]) = (a[j-1], a[j])
                x += 1
    return s, x

def puziko(a):
    s = 0
    x = 0
    for i in a:
        c=0
        for j in range(len(a)-1, 0, -1):
            s += 1
            if a[j] < a[j-1]:
                (a[j], a[j-1]) = (a[j-1], a[j])
                x += 1
                c += 1
        if c==0:
            return s, x

print(puz(a))
a=[8, 3, 4, 7, 1]
print(puziko(a))
