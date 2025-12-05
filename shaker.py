a=[8, 3, 4, 7, 1]
s=0
x=0
for i in a:
    for j in range(len(a)-1, 0, -1):
        s += 1
        if a[j] < a[j - 1]:
            (a[j], a[j - 1]) = (a[j - 1], a[j])
            x+=1
    for l in range(0, len(a)-1):
        s += 1
        if a[j] > a[j + 1]:
            (a[j], a[j + 1]) = (a[j + 1], a[j])
            x+=1

print(a)
print(s, x)
