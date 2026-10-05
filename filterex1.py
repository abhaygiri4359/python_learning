def positive(val):
    if(val>0):
        return True
    else:
        return False
def negative(val):
    return True if val<0 else False    
num=[1,2,3,4,5,6,7,8,-2,-2,-4,-5]
vall=filter(positive,num)
neg=filter(negative,num)
print(vall) # when we print filter object we only get memory object we must have to type cast any iterable object   
print(list(vall))
print(list(neg))