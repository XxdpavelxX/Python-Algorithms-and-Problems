__author__ = 'xxdpavelxx'

def square_rooter(number): # only works for perfect roots, otherwise returns an estimate
    x=0
    while x*x<number:
        x=x+1
    print "The square root is:",x

square_rooter(234235232154235)

