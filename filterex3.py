print("enter the words seprated by space")
lst=[words for words in input().split()]
print(lst)
a=list(filter(lambda word:word==word[::-1],lst)) 
print(a)