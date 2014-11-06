__author__ = 'xxdpavelxx'
#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks
#(5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little
#harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

#make_bricks(3, 1, 8) = True
#make_bricks(3, 1, 9) = False
#make_bricks(3, 2, 10) = True

def make_bricks(small, big, goal):
#Solution without loops
    x= goal%5
    if x==0 and big>=goal/5:
        return True
    if small>= goal-big*5:
        if small>=x:
            return True
        else:
            return False

    else:
        return False


#Solution with loops

    #current=0
    #big_used=0
    #small_used=0
    #while big_used<big and goal>= current+5:
     #   current=current+5
      #  big_used=big_used+1
       # if current == goal:
        #    return True

    #while small_used<small and goal>=current+1:
     #   current=current+1
      #  small_used=small_used+1
       # if current ==goal:
        #    return True

    #return False

if __name__=="__main__":
    print make_bricks(3, 1, 8)
    print make_bricks(3, 1, 9)
    print make_bricks(3, 2, 10)
    print make_bricks(6, 0, 11)

