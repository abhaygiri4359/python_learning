#program for wovel word
w=input("enter a word ")
lst=['a','i','o','u','u']
for i in w:
    if(i.lower() in lst ):
        print("it is vowel")
        break
    else:
        print("not a vowel")
        break