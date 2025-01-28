#transport
print("Your transport")
print("1.Car")
print("2.Bus")
choice=int(input("select your transport"))
if choice==1 :
    print("1.SUV/n")
    print("2.Electric/n")
    type=int(input(" which type of Car"))
    if type==1 :
        print("you have selected a SUV")
    else : 
        print("you have selected an Electric")

elif choice==2 :
    print("1.Volvo")
    print("2.Local")
    engine=int(input("which type of Bus"))
    if engine==1 :
        print("you have selected volvo ")
    else :
        print("you have selected Local")
    
else :
    print("Wrong transport")

   

