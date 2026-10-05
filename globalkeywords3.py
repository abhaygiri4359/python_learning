def update1():
    global a,b
    a=a+1
    b=b+1

def update2():
    global a,b
    a=a+1
    b=b+1
def update3():
    
    c=a+10*3
    d=b+10*3
    print("local {},{}".format(c,d))
a,b=10,20
print("before update 1 {} {} ".format(a,b))
update1()
print("after  update 1 {} {} ".format(a,b)) 
print("*"*100)
print("before update 2 {} {} ".format(a,b))
update2() 
print("after  update 1 {} {} ".format(a,b)) 
print("*"*100)
print("before update 3 {} {} ".format(a,b))
update3() 
print("after  update 3 {} {} ".format(a,b))
        