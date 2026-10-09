#program for finding sum of +ve and -Ve sum from list
import functools as x
print("enter the values seprated by ,")
values=[float(val) for val in input().split()]
print(values)
#+ve value
posval=list(filter(lambda x: x>=0,values ))
print(posval)
#-ve value
negval=list(filter(lambda x: x<0,values ))
print(negval)
#pos sum 
possum=x.reduce(lambda a,b:a+b,posval)
print(possum)
#negativce sum
negsum=x.reduce(lambda a,b:a+b,negval)
print(negsum)

