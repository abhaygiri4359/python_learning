import functools
lst=[12,34,21,23,21]
res=functools.reduce(lambda x,y:x+y,lst)
print(res)