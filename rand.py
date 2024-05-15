#number guessing game
import random

#all the guessed numbers and random number will be put into this list
#this function will find out the index of the random number
def index(lyst, gNum):

    for i in range(len(lyst)):
        if lyst[i] == gNum:
            return i

#random number put into the list
rNum = random.randint(1,100)
lyst = []
lyst.append(rNum)
num=-1

while(num!=rNum):

    num = int(input("Guess the number (1~100): "))
    lyst.append(num)
    lyst.sort()

    if len(lyst) > 2:

        i = index(lyst,rNum)

        # eliminate the possibility of out of range
        if i == len(lyst)-1:
            print(f"it's between {lyst[i-1]} and 100")
        else:
            print(f"it's between {lyst[i-1]} and {lyst[i+1]}")
    
    else:
        if num < rNum:
            print(f"it's between {num} and 100")
        
        if num > rNum:
            print(f"it's between {num} and 0")

    print("")


print("Correct!")
print("You win!")