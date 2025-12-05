a=[2, 3, 1, 5]
s=0
x=0
for i in range(1, len(a), 1):
    for j in range(i, 0, -1):
        s+=1
        if a[j] < a[j-1]:
            x+=1
            (a[j], a[j - 1]) = (a[j - 1], a[j])
print(a)
print(s, x)
