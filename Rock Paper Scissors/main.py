import random

# variables
choices = ['R','P','S']

cpu = random.choice(choices)

welcomeMessage1='Welcome to Rock Paper Scissors game User' +'\n' +"If you choose to play Rock input 'R' " +'\n'+\
                "If you choose to play Paper input 'P'"+'\n'+"If you choose to play Scissors input 'S'"
welcomeMessage2="To win: Rock('R') bangs Scissors('S')"+'\n'+"To win: Scissors('S') cuts Paper('P')"+'\n'+"To win: Paper('P') wraps Rock('R')"
print(welcomeMessage1,'\n',"-------LET'S PLAY-----",'\n',welcomeMessage2)

#Checking if the user wins and computer loses
while True:
    userChoice = input("Kindly input your choice in Capital Letters ('R','P','S'): ")

    if userChoice == 'R':
        if cpu == 'S':
            print(f"Player[Rock] : CPU[Scissor]")
            print("---You won.....Rock bangs Scissors")
            break

    if userChoice == 'P':
        if cpu == 'R':
            print(f"Player[Paper] : CPU[Rock]")
            print("---You won.... Paper wraps Rock")
            break

    if userChoice == 'S':
        if cpu == 'P':
            print(f"Player[Scissor] : CPU[Paper]")
            print("---You won... Scissor cuts Paper")
            break


#checking if the game is a tie
    if userChoice == "R":
        if cpu == "R":
            print(f"Player[Rock] : CPU[Rock]")
            print("----IT'S A TIE----")
            continue

    if userChoice == 'P':
        if cpu == 'P':
            print(f"Player[Paper] : CPU[Paper]")
            print("----IT'S A TIE----")
            continue

    if userChoice == 'S':
        if cpu == 'S':
            print(f"Player[Scissor] : CPU[Scissor]")
            print("----IT'S A TIE----")
            continue


#checking if the Computer wins and User loses

    if userChoice == 'R':
        if cpu == 'P':
            print(f"Player[Rock] : CPU[Paper]")
            print("--You Lost...Paper wraps Rock")
            break

    if userChoice == 'P':
        if cpu == 'S':
            print(f"Player[Paper] : CPU[Scissor]")
            print("--You Lost... Scissor cuts paper")
            break

    if userChoice == 'S':
        if cpu == 'R':
            print(f"Player[Scissor] : CPU[Rock]")
            print("--You Lost... Rock bangs Scissor")
            break
    else:
        print("Please check if the letter is correct and in capital form....")
        continue