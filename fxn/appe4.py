#defining a fxn for addimg of two numbers
def sum(a,b):
    c=a+b
    return a,b,c

x,y,z=sum(40,30)#functioncall with multiline assignment
print("thr sum =",x,y,z)
res=sum(10,20)
print(res)# it will retirn tuple 

print(res[0],res[1],res[2])
