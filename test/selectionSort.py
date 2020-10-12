#选择排序
from randomList import randomList

iList = randomList(20)

def selectionsort(iList):
    if len(iList) <= 1:
        return iList
    for i in range(0,len(iList)-1):
        if iList[i] != min(iList[i:]):
            minIndex = iList.index(min(iList[i:]))
            iList[i],iList[minIndex] = iList[minIndex],iList[i]
    return iList


if __name__ == '__main__':
    print(iList)
    print(selectionsort(iList))