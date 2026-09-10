#program for finding biggest in two number by using ternary operator
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=a if a>b else b if b>a else "both are equal"
print(c)
