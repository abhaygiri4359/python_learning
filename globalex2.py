def ai():
    domain='ai'# this are local variables
   # lang='python'# this are local variables
    print("for start {} you have to know {}".format(domain,lang))
lang='python'# you can define global before the function all anywhare    
def ml():
    domain='machine learning'# this are local variables
   # lang='python'# this are local variables
    print("for start {} you have to know {}".format(domain,lang))
#main function 
lang='python'#here python is global variables
ai()
ml()       