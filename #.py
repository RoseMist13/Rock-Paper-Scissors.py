#the rock paper scissors program

from random import randrange

def main():
    continue_game = 'y'
    
    while continue_game.lower() == 'y':
        user_weapon = get_user_weapon()
        computer_weapon, computer_num = get_computer_weapon()
        
        #this part shows the user, what they chose and what the computer chose
        print(f"\n\n Your weapon of choice:  {user_weapon}")
        print(f" The computer's number: {computer_num}")  
        print(f" The computer's weapon of choice: {computer_weapon}\n\n")
        
        determine_winner(user_weapon, computer_weapon)
        
        continue_game = input("Do you want a rematch? (y/n): ")

def get_user_weapon():#user input and their choice
    while True:
        choice = input(" Lets play a game \n You will choose from these 3 weapons (1-3): \n\n 1. Rock \n 2. Paper \n 3. Scissors \n\n Lets begin, shall we? :")
        
        if choice == '1':
            return "Rock"
        elif choice == '2':
            return "Paper"
        elif choice == '3':
            return "Scissors"
        else:
            print("That isn't a valid choice. Please choose a number between 1 and 3.")

def get_computer_weapon():#the random num generator
    computer_num = randrange(1, 4)
    if computer_num == 1:
        return "Rock", computer_num
    elif computer_num == 2:
        return "Paper", computer_num
    elif computer_num == 3:
        return "Scissors", computer_num

#the win or loss of the system
def determine_winner(user_weapon, computer_weapon):
    if user_weapon == computer_weapon:
        print("It's a tie")
        
    elif (user_weapon == 1 and computer_weapon == 3) or \
         (user_weapon == 2 and computer_weapon == 1) or \
         (user_weapon == 3 and computer_weapon == 2):
        print(" I lost, good job, you won")
    else:
        print(" Sorry but better luck next time\n\n")
        
        
        
        
if __name__ == "__main__":
    main()
    print ( "compteted by, pablo romero")
        
