import random,operator

def GenerateRandomArray(size,value):
    array = []
    for i in range(size):
        array.append(int((value+1)*random.random())-int((value)*random.random()))
    return array

def RightMethod(array):
    array.sort()
    return array

def bubble_sort(a):
    L = len(a)
    for j in range(0,L-1):
        for i in range(0,L-1-j):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
            #print(a)
    return a

def IsRight(times,size,value,func):
    succeed = True
    for i in range(times):
        arr1 = GenerateRandomArray(size,value)
        arr2 = arr1.copy()
        arr3 = arr1.copy()
        func(arr1)
        RightMethod(arr2)
        if not operator.eq(arr1,arr2):
            print(arr1)
            print(arr2)
            succeed = False
            print('Raw_array',arr3)
            break
    print('NICE' if succeed==True else 'WRONG')
IsRight(5000,20,20,bubble_sort)