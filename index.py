'''
1 for rock
0 for paper 
-1 for sissor
'''
import random
computer= random.choice([1,0,-1])

print("Game Rules: \nr : Rock, p : paper, s : sessiors")

user=input("Enter your choice: ")
dict= {"s": -1, "r": 1, "p":0}
if user not in dict:
    print("You are enterd a wrong Entry..")
    exit()

me=(dict[user])

new_dict= {-1: "Sissor", 0:"Paper", 1: "Rock"}
print(f"You Chosse {new_dict[me]}\nComputer Chosse {new_dict[computer]}")

if (computer==me):
    print("It's a draw!")
else:

    if(computer==1 and me==0):
        print("You Win!")
    elif(computer==1 and me==-1):
        print("You Lose!")
    elif(computer==0 and me==1):
        print("You Lose!")
    elif(computer==0 and me==-1):
        print("You Win!")
    elif(computer==-1 and me==0):
        print("You Lose!")
    elif(computer==-1 and me==1):
        print("You Win!")
    else:
        print("Something Went Wrong, Please Try again.")


