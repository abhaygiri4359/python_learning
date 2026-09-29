def incr():
    global a
    a=a+1
a=10
print(a)#before calling fxn
incr()
print(a)#after calling fxcn
# this program will not give error because pvm treat global variavle in fxn defination 
    