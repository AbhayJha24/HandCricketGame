# Import random for implementing random numbers

import random

# Define global variables for final scores and initialise them to Zero

playerFinalScore = 0
computerFinalScore = 0

# Define the batting function

def batting(second = 0, prevScore = 0):

    score = 0

    while(True):
        print("Enter a no. from 1 to 6")
        playerNo = int(input(""))
        computerNo = random.randint(1, 6)

        if(playerNo == computerNo):
            print("")
            print("Out!")
            print("")
            print("Computer' s number was ", computerNo)
            print("")
            break
        elif(playerNo < 1 or playerNo > 6):
            print("Invalid number chosen... Try again")
            continue
        else:
            score += playerNo
            print(playerNo, " Runs!")
            print("Computer' s number was ", computerNo)
            if(second == 1 and prevScore < score):
                break
            else:
                continue

    print("")
    print("You scored a total of ", score, " Runs!")
    return score

# Define the bowling function

def bowling(second = 0, prevScore = 0):

    compScore = 0

    while(True):
        print("Enter a no. from 1 to 6")
        playerNo = int(input(""))
        computerNo = random.randint(1, 6)

        if(playerNo == computerNo):
            print("")
            print("Out!")
            print("")
            print("Computer' s number was ", computerNo)
            print("")
            break
        elif(playerNo < 1 or playerNo > 6):
            print("Invalid number chosen... Try again")
            continue
        else:
            compScore += computerNo
            print("Computer Scored ", computerNo, " Runs!")
            print("Your number was ", playerNo)
            if(second == 1 and prevScore < compScore):
                break
            else:
                continue

    print("")
    print("Computer scored a total of ", compScore, " Runs!")
    return compScore

# Define the score checker function

def check(sc1,sc2):
    if(sc1 > sc2):
        print("You Win!")

    elif(sc2 > sc1):
        print("You Lose... Better Luck next time!")

    else:
        print("Match Draw, What a match!")

# Main game begins here

while(True):
    print("Welcome, this is the game of hand cricket!")
    print("")
    print("Rules: You have to enter a number from 1 to 6 and computer also randomly chooses a number from 1 to 6. While you are batting, you score as many runs as the number entered by you and again you enter a new number from 1 to 6 and so on till you get out. If your number and the computer' s number are the same then you are out. While bowling, computer scores as many runs as the number entered by the computer and you also enter a random no as before and again the same thing repeats till computer gets out by the same number matching procedure as mentioned above. You can choose to bowl or bat first. The one batting second can win by scoring more runs than the former. The one who scores more wins the game. Good Luck!")
    print("")
    print("You always win the toss here")
    print("What is your choice 1-> Batting, 2-> Bowling, 0-> Quit")
    choice = int(input(""))
    print("")

    # Initialise the final scores

    playerFinalScore = 0
    computerFinalScore = 0

    # On the basis of choice, player can either bat or bowl first

    if(choice == 1):
        print("Your batting begins!")
        print("")
        playerFinalScore = batting()
        print("End of the Innings!")
        print("")
        print("Your bowling begins!")
        print("")
        computerFinalScore = bowling(1,playerFinalScore)

    elif(choice == 2):
        print("Your bowling begins!")
        print("")
        computerFinalScore = bowling()
        print("End of the Innings!")
        print("")
        print("Your batting begins!")
        print("")
        playerFinalScore = batting(1,computerFinalScore)

    elif(choice == 0):
        break

    else:
        print("Invalid number chosen... Try again")
        print("")
        continue

    # Finally check the score and declare the winner

    print("")
    check(playerFinalScore,computerFinalScore)
    print("")