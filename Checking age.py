#Check age
age=int(input("Enter your age"))
if age < 13 :
    print("you are a child")
elif 13 <= age < 20 :
    print("you are a teenager")
elif 20 <= age < 60:
    print("You are an adult")
else :
    print(" you are a senior ")