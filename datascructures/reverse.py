a=int(input("enter the number"))
num=a
reverse=0
x=0
while(num>0):
    x=num%10
    reverse=reverse*10+x
    num=num//10
print(reverse)    
    
    