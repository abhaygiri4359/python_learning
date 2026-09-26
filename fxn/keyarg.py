#keywords agrs
def prints(a,b,c,d):
    print("{},{},{},{}".format(a,b,c,d))
print("_______________")
prints(10,20,30,40)#function call with positional arguments
prints(d=40,a=10,b=20,c=30)#function call with keywords arguments
#prints(d=40,c=30,10,20) this will give error
