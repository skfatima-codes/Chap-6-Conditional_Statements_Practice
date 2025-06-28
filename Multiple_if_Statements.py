a=int(input("Enter your age"))
# if statement 1
if(a%2==0):
    print(a ,"is a even no")
    # end of if statement 1(This if is independent)
    # if statement no 2
if(a>18):
    print("You are the above age of consent")
elif(a<0):
    print("You are entering an invalid negative age") # space before print is indent(Indentation)
else:
    print("You are below the age of consent")#Last elif will execute only if all conditions inside elif failed.
    #  end of if statement 2
    
print("End of the program")