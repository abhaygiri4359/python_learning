import shares

def display(d):
    print("_"*57)
    print("\tshare\tprice")
    for i,j in d.items():
        print(i,j)
d=shares.sharesinfo()
display(d)        