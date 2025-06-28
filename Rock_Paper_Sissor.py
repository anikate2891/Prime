'''
1 for rock
0 for paper 
-1 for sissor
'''
print("Let's Play ROCK / PAPER / SISSORS")
print("Game Rules: \nr : Rock, p : paper, s : sessiors")
import random
computer=random.choice ([1,0,-1]) #1
user=input("Enter your Choice: ") #r

dict={"r":1, "p":0, "s":-1}
if user not in dict:
    print("You are entry the wrong data..")
    exit()
me=dict[user]

new_dict={1:"rock", 0:"paper", -1:"sissor"}
print(f"You Choose {new_dict[me]}\nComputer Choose {new_dict[computer]}")

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
