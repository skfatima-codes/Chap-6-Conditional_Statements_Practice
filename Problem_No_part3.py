# Problem No 2_3
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your msg")  # Fix is here!

if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This comment is a spam")
else:
    print("This comment is not a spam")
