__author__ = 'xxdpavelxx'
def smallest(array):
    small=array[0]
    index=0
    for i in range(1,len(array)):
        if small>array[i]:
            small = array[i]
            index=i
    return small



print smallest([1,2,3,0,4,-1,5,6,-2])

def selectionSort(arr):
    newArray=[]
    for i in range(len(arr)):
        small_num= smallest(arr)
        newArray.append(arr.pop(small_num))

