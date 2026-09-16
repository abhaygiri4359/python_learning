#program for taking positive and negative from list
s=[-2,23,-34,-45,33,50,-67,12,44]
nop=0
non=0
print("printing +ve number in list")
for ch in s:
    
    if(ch<=0):
        continue
    else:
        nop=nop+1
        print(ch)
print(nop)
print("printing -ve numbers")
for ch in s:
    
    if(ch>0):
        continue
    else:
        non=non+1
        
        print(ch)
print(non)        
        