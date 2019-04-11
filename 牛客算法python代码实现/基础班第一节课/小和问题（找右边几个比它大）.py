import random




def GenerateRandomInt(l,r,size):
    a = random.sample(range(l,r),size)
    return a


def smallSum(arr):
    # 当数组为空或者只有一个数，小和为0
    if not arr or len(arr) < 2:
        return 0
    return mergeSum(arr, 0, len(arr) - 1)


# 求和函数
def mergeSum(arr, l, r):

    '''
    起到分组求和的作用
    :param arr:原数组
    :param l: 划分过后的数组的左指针
    :param r: 划分过后的数组的右指针
    :return: 返回全部小和之和
    '''
    # 如果划分的数组的左指针和右指针重合，则没有产生小和，返回0
    if l == r:
        return 0
    # mid是划分的中点，其数值表示在原数组arr的索引位置
    mid = (l + r) // 2
    left = mergeSum(arr, l, mid)
    right = mergeSum(arr, mid + 1, r)
    return left + right + merge(arr, l, mid, r)


# 合并时求小和
def merge(arr, l, m, r):

    '''
    起到榨取与排序的作用，先榨取在排序
    :param arr:程序一开始传入的原数组
    :param l: 将要合并时的数组左指针
    :param mid: 合并时在数组中的中点索引位置
    :param r: 将要合并时的数组右指针
    :return: 返回合并时产生的小和，在合并时只会求解  两数组右边数组的数对左边数组的数产生的小和。
    '''

    ret = []
    # p1是左边数组的第一个索引位
    p1 = l
    # p2是右边数组的第一个索引位
    p2 = m + 1
    res = 0

    while p1 <= m and p2 <= r:
        # 求解右边数组中的数对左边数组中的数产生的小和
        # 如果p1索引上的数比p2上的索引数小，则p2后面的数都比p1的数大，都会贡献小和。产生小和：arr[p1]*(r-p2+1)
        res += (r - p2 + 1) * arr[p1] if arr[p1] < arr[p2] else 0
        if arr[p1] < arr[p2]:
            ret.append(arr[p1])
            p1 += 1
        else:
            ret.append(arr[p2])
            p2 += 1
    while p1 <= m:
        ret.append(arr[p1])
        p1 += 1
    while p2 <= r:
        ret.append(arr[p2])
        p2 += 1
    # 将局部排序好的ret 去 替换原数组arr
    arr[l:r + 1] = ret
    return res


# list1 = [1,2,3,4,5,6,7,8]
# f1 = smallSum(list1)
# print(f1)

#下边是对数器
def GenerateRandom(size,value):
    '''
    随机数产生器
    :param size:
    :param value:
    :return:
    '''

    c = []
    for i in range(size):
        c.append(int((value+1)*random.random())-int(value*random.random()))
    return c

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
#print(IsRight([1,2,3,4,5,6,7,8]))

def CopyArr(arr):
    '''
    复制一份数组
    :param arr:
    :return:
    '''
    if not arr :
        return 0
    res = []
    for i in range(len(arr)):
        res.append(arr[i])
    return res

def IsEqual(a1,a2):
    if not a1 or not a2:
        return False
    if not a1 and not a2:
        return True
    if len(a1)!=len(a2):
        return False
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            return False
    return True

def PrintArr(a):
    if not a:
        return
    for i in range(len(a)):
        print(str(a[i])+' ')
    return

def Main():
    TestTimes = 50000
    MaxSize =  50
    MaxValue = 100
    succeed = True
    for i in range(TestTimes):
        arr1 = GenerateRandom(MaxSize,MaxValue)
        arr2 = CopyArr(arr1)
        if smallSum(arr1) != IsRight(arr2):
            succeed = False
            PrintArr(arr1)
            PrintArr(arr2)
            break
    print('NICE' if succeed == True else 'Fucking Fucked')

if __name__ == '__main__':
    Main()

#PrintArr([1,2,3])


#print(CopyArr([123,56]))





