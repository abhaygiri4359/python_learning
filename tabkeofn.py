#table of n numbers
import sys
i=int(input("ente last table number"))
if(i<=0):
    sys.exit()
else:
    for n in range(1,i+1):
        print("-"*50)
        print("table for ",n)
          
        for j in range(1,11):
            print("{}*{}={}".format(n,j,j*n))    