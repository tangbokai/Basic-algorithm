def IsRight(arr):
    '''
    绝对正确好想的办法
    :param arr:
    :return:
    '''
    if not arr or len(arr)<2:
        return 0
    res = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                res+=arr[i]


    return  res
print(IsRight([1,2,3,4,5,6,7,8]))