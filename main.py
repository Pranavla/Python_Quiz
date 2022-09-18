print("It's Quiz time,welcome")
intro=input("Do you want to play? ").lower()
if intro!="yes":
    quit()
print("Okay! Let's Play")
s=0
#Que1
ans=input("1.Is python case sensitive when dealing with identifiers \nanswer:").lower()
if ans=="no":
    print("You are correct:)")
    s+=1
else:
    print("Wrong answer!")
#Que2
ans=input("2.Which keyword is used for function in python language? \nanswer:").lower()
if ans=="def":
    print("You are correct:)")
    s+=1
else:
    print("Wrong answer!")
#Que3
ans=input("3.What does pip stand for in python? \nanswer:").lower
if ans=="preferred installer program":
    print("You are correct")
    s+=1
else:
    print("Wrong answer!")
#Que4
ans=input("4.What is called when a function is defined inside a class? \nanswer:").lower()
if ans=="method":
    print("You are correct:)")
    s+=1
else:
    print("Wrong answer!")
#Que5
ans=input("5.Lambda function is also called _____ \nanswer:").lower()
if ans=="anonymous function":
    print("You are correct:)")
    s+=1
else:
    print("Wrong answer!")
print("Congrats!,you got " + str(s) + " Score out of 5")