
# username=input("Enter the username")
# if(len(username)<=10):
#     print("username contains 10 characters")
# else:
#     print("Doesnot contain 10 characters")

# Problem 5
# l=("Har","Fat","Gat")
# name=input("Enter the name")
# # if(name=="Har"):
# if name in l:
#     print("Name has been found by the user")
# else:
#     print("Not found")

# Problem 6
# marks=int(input("Enter your marks"))
# if(marks<=100 and marks>=90):
#     grade="Ex"
# elif(marks<=90 and marks>=80):
#    grade="A"
# elif(marks<=80 and marks>=70):
#    grade="B"
# elif(marks<=70 and marks>=60):
#    grade="C"
# elif(marks<=60 and marks>=50):
#    grade="D"
# elif(marks<=50):
#    grade="F"

# print("YOUR GRADE IS:",grade) #we remove indentation b/c now we are not in elif ladder
    
# Problem no 7
post="Henry is good Harry is very good and henry is great"
# if("Harry" in post):
if("Harry".lower() in post.lower()):
    print("The post is talking about harry")
else:
    print("The post is not talking about harry")