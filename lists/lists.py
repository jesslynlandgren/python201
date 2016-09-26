import numpy

def sumList(exList):
    sumtemp = 0
    for i in exList:
        sumtemp += i
    return sumtemp

def largest(exList):
    largest = 0
    for num in exList:
        if num > largest:
            largest = num
    return largest

def smallest(exList):
    smallest = exList[0]
    for num in exList:
        if num < smallest:
            smallest = num
    return smallest

def evens(exList):
    for num in exList:
        if num % 2 == 0:
            print num

def positive(exList):
    for num in exList:
        if num >0:
            print num

def positiveList(exList):
    newList = []
    for num in exList:
        if num >0:
            newList.append(num)
    return newList

def multList(exList,factor):
    newList = []
    for num in exList:
        newList.append(num*factor)
    return newList

def multVec(exList1, exList2):
    newList = []
    for i in range(0,len(exList1)):
        newList.append(exList[i]*exList2[i])
    return newList

def matAdd(mat1, mat2):
    newMat = []
    for i in range(0,len(mat1)):
        newMat.append([])
        for j in range(0,len(mat1[i])):
            newMat[i].append('X')
            newMat[i][j] = mat1[i][j] + mat2[i][j]
    return newMat

def dedup(exList):
    newList = []
    counts = []
    for i in exList:
        counts.append(exList.count(i))
    for i in range(0, len(counts)):
        if counts[i] == 1:
            newList.append(exList[i])
    return newList

    # newList = list(set(exList))
    # return newList

def matMult(mat1, mat2):
    prodMat = []
    for i in range(0,len(mat1)):
        prodMat.append([])
        for j in range(0,len(mat1[i])):
            prodMat[i].append('X')
    prodMat[0][0] = (mat1[0][0] * mat2[0][0]) + (mat1[0][1] * mat2[1][0])
    prodMat[0][1] = (mat1[0][0] * mat2[0][1]) + (mat1[0][1] * mat2[1][1])
    prodMat[1][0] = (mat1[1][0] * mat2[0][0]) + (mat1[1][1] * mat2[1][0])
    prodMat[1][1] = (mat1[1][0] * mat2[0][1]) + (mat1[1][1] * mat2[1][1])
    return prodMat

    # return numpy.dot(mat1,mat2)

exList = [-2,-1,0,1,2,3,4,5,6,7,8,9,10]
exList2 = [-2,-1,0,1,2,3,4,5,6,7,8,9,10]
exMat1 = [[1, 3],
          [2, 4]]
exMat2 = [[5, 2],
          [1, 0]]
exList3= [-2,-1,0,1,2,3,4,1,2,3,4,5]


print sumList(exList)
print largest(exList)
print smallest(exList)
print '**********'
evens(exList)
print '**********'
positive(exList)
print '**********'
print positiveList(exList)
print '**********'
print multList(exList,2)
print '**********'
print multVec(exList,exList2)
print '**********'
print matAdd(exMat1,exMat2)
print '**********'
print dedup(exList3)
print '**********'
print matMult(exMat1,exMat2)
