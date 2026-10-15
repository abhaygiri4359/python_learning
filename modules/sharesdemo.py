import shares,time,importlib

def display(d):
    print("_"*57)
    print("\tshare\tprice")
    for i,j in d.items():
        print(i,j)
d=shares.sharesinfo()
display(d) 
print("i am going to sleep for 15 sec")
time.sleep(15) 
print("i am coming after 15 sec ")
importlib.reload(shares)
d=shares.sharesinfo() 

print(d)
     