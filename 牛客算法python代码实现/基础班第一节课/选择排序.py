import random
a = random.sample(range(1,100),20)
print(a)

l = len(a)

for i in range(l-1):
    maxindex = i
    for j in range(i+1,l):
        if a[maxindex]>a[j]:
            maxindex = j
    a[i],a[maxindex]=a[maxindex],a[i]
    print(a)
print(a)
