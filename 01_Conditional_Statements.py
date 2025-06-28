# if elif else ladder
a=int(input("Enter your age"))
if(a>18):
    print("You are the above age of consent")
elif(a<0):
    print("You are entering an invalid negative age")
elif(a==0):
    print("You are entering an invalid age")
else:
    print("You are below the age of consent") # space before print is indent(Indentation)
    
print("End of the program")