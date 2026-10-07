print("enter the list of value ")
lst=[float(val) for val in input().split()]
print("the list is ",lst)
sqar=list(map(lambda val:val**2,lst))
print("the square of list id ",sqar)
root=list(map(lambda val:round(val**0.5,2),lst))
print("the sqroot of list id",root)

