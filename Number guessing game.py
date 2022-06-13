from random import randint 
Easy_Turns = 10
Hard_Turns = 5
logo = '''
   _____                       _   _                 _               
  / ____|                     | \ | |               | |              
 | |  __ _   _  ___  ___ ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/ |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                
'''                       
def Check_answer(guess,turns,answer):
    if guess > answer:
        print("Too high ")
        return turns - 1
    elif guess < answer:
        print("Too low ")
        return turns - 1
    else:
        print(f"You got it right! {answer}")
def set_difficulty():
    Level = input("Choose a difficulty level 'easy' or 'hard' ")
    if Level == "easy":
        return Easy_Turns
    elif Level == "hard":
        return Hard_Turns
def game():
    print(logo)
    print("Welcome! to Number guessing game ")
    answer= randint(1,100)
    turns = set_difficulty()
    guess = 0
    while guess!=answer:
        print(f"You have {turns} attempts remaining ")
        guess = int(input("Make a guess : "))
        turns = Check_answer(guess,turns,answer)
        if turns == 0:
            print("You lost it ")
        elif guess!=answer:
            print("Guess again")
game()
            
        