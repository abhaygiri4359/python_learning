print("enter the numericals for list 1")
lst1=[float(val) for val in input().split()]
print("enter the numericals for list 2")
lst2=[float(val) for val in input().split()]
if len(lst1)>len(lst2):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0.0)
elif len(lst1)>len(lst2):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0.0)        
print(lst1,lst2) 
#Now List Values becomes equal and add them by using map()
lst3=list(map(lambda x,y: x+y, lst1,lst2))
print("-"*60)
print("\tFirst List\tSecond List\tSum List")
print("-"*60)
for no1,no2,no3 in zip(lst1,lst2,lst3):
    print("\t{}\t\t{}\t\t{}".format(no1,no2,no3))
print("-"*60)       