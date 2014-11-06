__author__ = 'xxdpavelxx'

#Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.

#array123([1, 1, 2, 3, 1]) = True
#array123([1, 1, 2, 4, 1]) = False
#array123([1, 1, 2, 1, 2, 3]) = True

def array123(nums):
    check_list=[1,2,3]
    for x in nums:
        if x in check_list:
            check_list.remove(x)
    if len(check_list)==0:
        return True
    else:
        return False


if __name__=="__main__":
    print array123([1, 1, 2, 3, 1])
    print array123([1, 1, 2, 4, 1])
    print array123([1, 1, 2, 1, 2, 3])