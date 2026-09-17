#demonstrating inner loop
for i in range(1,6):
    
    print("value of outer loop= ",i)
    print("="*40)
   
    for j in range(1,4):
        print("value of inner loop=",j)
    else:
        print("inner loop out of bound")
else:
    print("inner loop out of bound")            