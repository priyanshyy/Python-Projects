import random as rdm

again=True
print("------Rolling started------")
while again:
    print("\n<<  ",rdm.randint(1,6),"  >>")
    roll=input("Want to roll the dice again ? y/n : ")
    if roll.lower()=='y':
        continue
    else:
         print("\n------Rolling stopped------")
         break
     