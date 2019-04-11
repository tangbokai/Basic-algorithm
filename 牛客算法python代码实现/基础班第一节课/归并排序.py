import random
a = random.sample(range(1,100),20)
print(a)
l = len(a)

def merge(a,b):
    #合并两个有序数组
    c = []

    a1 = 0
    a2 = 0


    while a1 < len(a) and a2 < len(b):
        if  a[a1]>=b[a2]:
            c.append(b[a2])
            a2+=1

        else:
            c.append(a[a1])
            a1+=1
    if a1 == len(a):
        for i in b[a2:]:
            c.append(i)
    else:
        for i in a[a1:]:
            c.append(i)
    return  c


def merge_sort(a):
    # 分治排序
    if len(a) ==1:
        return a
    mid = int(len(a) / 2)
    sort_left = merge_sort(a[:mid])
    sort_right = merge_sort(a[mid:])

    return merge(sort_left,sort_right)
    #递归函数真正起作用的地方   以前就是负责一半一半的分开

b = merge_sort(a)
print(b)