def dispvalue(obj):
    print("type of obj=",type(obj))
    print("number of value={}".format(len(obj)))
    print("_______________________________")
    if(type(obj)==dict):
        for key,value in obj.items():
            print("{}:{}".format(key,value))
    else:
                
        for val in obj:
            print(val)
    print("____________________________________")    
lst=[1,2,3,4,5,6,True,"abhay",23]
dispvalue(lst)
tpl=(1,2,3,"abhaygiri",True,"hello")
dispvalue(tpl)
st={1,34,32,45,32,False,True,"Abhay"}
dispvalue(st)
dispvalue(())
dispvalue([])
dispvalue({})
dispvalue(set())
print("___________________________________________________")
d={1:"Abhay",2:"ayush",3:"index",4:"sahil",5:"abhi"}
dispvalue(d)

