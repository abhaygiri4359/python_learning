print("converting one datatype to another")
print("="*50)
print("press one for decimal to binary ")
print("press two for decimal to octal ")
print("press three for decimal to hexal ")
print("press four for binary to decimal ")
print("press five for binary to decimal ")
print("press six for binary to hexal")
print("press seven for octalo to binaty ")
print("press eight for octal to decimal")
print("press nine for octal to hexadecimal")
print("press ten for hexal to binary")
print("press eleven for hexal to octal")
print("press twelve for hexal to decimal")
choice=int(input("enter your choice"))
match(choice):
    case 1|2|3:
        dn=int(input("enter the decimal number"))
        x=bin(dn)
        print("binary of{} is {}".format(dn,x))
        y=oct(dn)
        print("octal of {} is {}".format(dn,y))
        z=hex(dn)
        print("hexal of {} is {}".format(dn,z))
    case 6|4|5:
        bn=input("enter your number 0b")
        x=int(bn,2)
        print("hexal of {} is {}".format(bn,hex(x)))
        print("decimal of {} is {}".format(bn,x))
        print("octal of {} is {}".format(bn,oct(x)))











