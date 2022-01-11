#Taking input from the user...

x=str(input("x="))

#Defining the lenghth of the string...

y=len(x)

#Applying conditions and giving print command to the string...

if x.isprintable():
    print("Reverse x :",x[y::-1])
else:
    print(" Error! Data provided, is not a string!")