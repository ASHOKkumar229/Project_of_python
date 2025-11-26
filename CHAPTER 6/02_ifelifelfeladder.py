a = int(input("Enter you age: "))
#if elif else ladder 
if(a>=18):
    print("You are above then age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invild age ") 

elif(a==0):
    print("You are entering 0 which is  not a  valid age  ")       

else:
    print("You below the age of consent")


print("End of program")