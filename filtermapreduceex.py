#salary under range of o to 1000 negative and more than thousand not aloud
print("enter the list of slary ranges 0 to 1000")
olsal=[float(sal) for sal in input().split()if 0<=float(sal)<=1000]
print("the salary is ")
print(olsal)
sal0_500=list(filter(lambda s: s<=500,olsal))
print(list(sal0_500))
sal501_1000=list(filter(lambda s: 500<s<=1000,olsal))
print(list(sal501_1000))
#10% hike in  0 to 500 salary
hike10=list(map(lambda s:s+s*1/10,sal0_500))
print(hike10,)
hike20=list(map(lambda s:s+s*1/5,sal501_1000))
print(hike20,)