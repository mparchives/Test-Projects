#number guessing game
import random

#all the guessed numbers and random number will be put into this list
#this function will find out the index of the random number
def index(lyst,r):

    for i in range(len(lyst)):
        if lyst[i]==r:
            return i

#random number put into the list
ran = random.randint(1,100)
lyst = []
lyst.append(ran)
num=-1

while(num!=ran):

    num = int(input("Guess the number (1~100): "))
    lyst.append(num)
    lyst.sort()

    if len(lyst) > 2:

        i = index(lyst,ran)

        # eliminate the possibility of out of range
        if i == len(lyst)-1:
            print(f"it's between {lyst[i-1]} and 100")
        else:
            print(f"it's between {lyst[i-1]} and {lyst[i+1]}")
    
    else:
        if num < ran:
            print(f"it's between {num} and 100")
        
        if num > ran:
            print(f"it's between {num} and 0")

    print("")


print("Correct!")
print("You win!")