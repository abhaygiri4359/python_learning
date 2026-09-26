num=int(input("entere a number"))
a=len(str(num))
x=num
arm=0
while(x>0):
    r=x%10
    arm=arm+r**a
    
    x=x//10
print(arm)    