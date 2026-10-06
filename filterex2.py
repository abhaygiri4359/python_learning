lst=[int(val) for val in input().split()]
x=list(filter(lambda val: True if val>0 else False,lst))
print(x)