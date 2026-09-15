#demonstrating break keyword
#program for chacking wheather it is prime or not
n=int(input("enter the number"))
count=0
if(n<0):
    print("enter number grater than zoro")

else:
    
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count>0):
        print("it is a prime number")
    else:
        print("not a prime number")        
    
               