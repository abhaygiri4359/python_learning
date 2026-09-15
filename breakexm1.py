#program for demonstrating break keyword
#My requirement is to to print PYTH only without using indexing and slicing
print("foe loop without break keyword")
s="PYTHON"
for ch in s:
    print(ch)
else:
    print("for loop else part")    
print("="*100)    
    
print("for loop with break keyword")
s="PYTHON"
for ch in s:
    if(ch=='O'):
        break
    else:
        print(ch,end='')
        
else:
    
    print("for loop else part")
print()
print("program executed")            