#even od with positive if user enter -ve then invalid input
a=float(input("enter the number"))
res="Invalid input" if a<0 else "even" if a%2==0 else "odd"
print(res)