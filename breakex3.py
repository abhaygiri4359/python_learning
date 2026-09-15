# program for demonstrating break
s="MISSISSIPPI"
ictr=0
for ch in s:
    
    if(ch=='I'):
        ictr+=1
    if(ictr==2):    
        break
        
        
    else:
        print(ch)