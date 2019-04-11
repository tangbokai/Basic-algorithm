import random
a = random.sample(range(1,20),10)
print(a)
def getMax(arr,l,r):
    if l==r:
        return arr[l]
    mid = int((l+r)/2)
    maxleft = getMax(arr,l,mid)
    maxright = getMax(arr,mid+1,r)
    return max(maxleft,maxright)

b = getMax(a,0,len(a)-1)
print(b)