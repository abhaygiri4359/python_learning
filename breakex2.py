#break second example in while lopp
#requriment id to display PYT onlu without using indexing and slicing
s="PYTHON"
print("without break statement")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("while lopp else part")
print("______________________"*5)
print("with break keyword")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
    if(s[i]=="H"):
        break
    
    

        
else:
    print("else part")
print("program executed")                    