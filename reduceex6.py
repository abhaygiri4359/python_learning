# program for concatinating group of words and making list
import functools as fc
print("enter the words seprated by ,")
val=[word for word in input().split(",")]
x=fc.reduce(lambda k,v:k+" "+v,val)
print(x)
