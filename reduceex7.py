# program for concatinating group of words and making list
import functools as fc
def fxn(k,v):
    return k+" "+v
print("enter the words seprated by ,")
val=[word for word in input().split(",")]
x=fc.reduce(fxn,val)
print(x)