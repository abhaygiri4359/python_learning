def typefxn(value):
    if(type(value)==int):
        print("{} is int type".format(value))
    elif(type(value)==float):
        print("{} is float type".format(value))
    elif(type(value)==list):
        print("{} is list type".format(value))
    elif(type(value)==set):
            print("{} is set type".format(value))
    elif(type(value)==tuple):
            print("{} is tuple type".format(value))
    elif(type(value)==str):
            print("{} is str type".format(value))
    elif(type(value)==complex):
            print("{} is complex type".format(value)) 
typefxn({1,3,4}) 
typefxn(1)                          