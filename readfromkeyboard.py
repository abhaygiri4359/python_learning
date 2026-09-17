# readind from keyboard
i=int(input("enter the nuber of data you want to input"))
if(i<0):
    print("please enter valid number")
else:
    lst=[]
    for n in range(1,i+1):
        
         print("ente the {} value".format(n))
         j=int(input())
         lst.append(j)
print(lst)    
