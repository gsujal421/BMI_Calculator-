import random

operations =['rock','scissor','paper']
user = input("Enter choice:").lower()   #user input
# if(user==user.upper()):
#     print (user.lower())
computer_choice= random.choice(operations)   
print(computer_choice)

if user not in operations:
    print("Invalid \nPlease try again")

elif user == computer_choice:
    print("Tie")
elif (user== 'rock' and computer_choice=='scissor') or( user=='paper' and computer_choice=='rock' ) or (user=='scissor' and computer_choice=='paper') :
    print("You Win")

else:
     print("You Loose")
