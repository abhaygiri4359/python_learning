#while loop in whilw loop
i=1

while(i<6):
    print("-"*50)
    print("outer loop =",i)
    i=i+1
    j=1
    print("-"*50)
    while(j<=3):
        print("inner loop=",j)
        j=j+1
    else:
        print("inner loop out of bound")
        
else:
    print("outer loop out of bound")        