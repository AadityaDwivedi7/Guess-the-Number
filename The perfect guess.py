import random
randnumber = random.randint(1, 100)

userguess = None
guesses = 0 

while(userguess != randnumber):
    userguess = int(input("Enter your guess: "))
    guesses += 1
    
    if (userguess==randnumber):
        print("you guessed it right")

    else:
        if(userguess>randnumber):
            print("You guessed it wrong! More smaller needed!")

        else:
            print("you guessed it wrong! Enter a larger number!")



print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if (guesses<hiscore):
    print("You have just broken the highscore")

with open("hiscore.txt", "w") as f:
    f.write(str(guesses))

