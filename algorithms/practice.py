__author__ = 'xxdpavelxx'
def foo(x=10):
   def bar(y=20, z=30):
       return z * (x + y)
   return bar

result = foo(1)(2, 3)
print result