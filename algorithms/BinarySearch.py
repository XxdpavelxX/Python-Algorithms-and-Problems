__author__ = 'xxdpavelxx'
def binary(list,value):
    high=len(list)-1
    low = 0
    attempts=1

    while low <= high:
        mid = (low+high)/2
        guess=list[mid]

        if guess>value:
            high = mid-1
            attempts=attempts+1

        elif guess<value:
            low = mid+1
            attempts=attempts+1

        elif guess == value:
            return mid,attempts


    return "The value is not in the list"

print binary([1,2,3,4,5,6,7],1)
