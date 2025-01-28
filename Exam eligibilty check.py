#Examattendence check
medical_cause=(input("cause is Y or N"))
atten=int(input("Enter your attendence"))
if medical_cause=="Y" :
    print("You are allowed")
else :
    if atten>=75 :
        print("you are allowed")
    else :
        print("you are not allowed")
    

    
    