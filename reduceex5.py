import functools
print("enter the value seprated by space")
value=[float(val) for val in input().split()]
value.sort(reverse=True)
print(value)
val=functools.reduce(lambda k,v:k if k>v else v,value)
print(val)