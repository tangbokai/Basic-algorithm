import random

a = random.sample(range(1,100),20)

print(a)
l = len(a)
for i in range(1,l):
    index = i
    for j in range(i-1,-1,-1):
        if a[index]<a[j]:
            a[index],a[j] = a[j],a[index]
            index-=1
        print(a)
print(a)