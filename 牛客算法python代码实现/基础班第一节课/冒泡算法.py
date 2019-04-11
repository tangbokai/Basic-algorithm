import random
a = random.sample(range(1,100),20)
print(a)


def bubble_sort(a):
    L = len(a)
    for j in range(0,L-1):
        for i in range(0,L-1-j):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
            print(a)
    return a

bubble_sort(a)
print(a)


