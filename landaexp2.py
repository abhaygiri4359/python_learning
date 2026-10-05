#biggest of two numbers
bigop=lambda a,b: a if a>b else b if b>a else "both are equal"
print(bigop(20,20))