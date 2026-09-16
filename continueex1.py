#demonstrating continue
s="PYTHON"
for ch in s:
    print(ch,end="")
else:
    print()
    print("for lopp else statement")
for ch in s:
    if(ch=='T'):
        continue
    print(ch,end="")
    
else:
    print()
    print("for loop else part")            