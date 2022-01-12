import random
import game

user_lives = 3
com_lives = 3
user_score = 0
com_score = 0
draw = 0

game.rules()

while True:
    
    if(game.check(user_lives, com_lives, user_score, com_score, draw) != True):
        user_lives = 3
        com_lives = 3
        user_score = 0
        com_score = 0
        
        if(game.again() == False):
            break
        
        
    user = game.Input()
    
    if (user == "status"):
        game.status(user_lives, com_lives, user_score, com_score, draw)
        user = game.Input()
    
    elif (user == "exit"):
        game.Exit(user_score, com_score, draw)
        break
    
        
    option = ["rock", "paper", "scissors"]
    computer = random.choice(option);
    print("computer chosed: ", computer)
    
    #......duplicates
    if (user == computer):
        print('draw')
        draw = draw + 1
        print("-------------------------------------------------")
    
    #........user is rock
    if(user =="rock" and computer == "paper"):
        print("computer wins");
        print("-------------------------------------------------")
        com_score = com_score + 1
        user_lives = user_lives - 1
    elif(user =="rock" and computer == "scissors"): 
        print("user wins")
        print("-------------------------------------------------")
        user_score = user_score + 1 
        com_lives = com_lives - 1
    
    
    #........user is paper
    if(user =="paper" and computer == "rock"): 
        print("computer wins")
        print("-------------------------------------------------")
        com_score = com_score + 1 
        user_lives = user_lives - 1
    elif(user =="paper" and computer == "scissors"): 
        print("user wins")
        print("-------------------------------------------------")
        user_score = user_score + 1 
        com_lives = com_lives - 1
        
    
    #........user is scissors
    if(user =="scissors" and computer == "rock"): 
        print("computer wins")
        print("-------------------------------------------------")
        com_score = com_score + 1 
        user_lives = user_lives - 1
    elif(user =="scissors" and computer == "paper"): 
        print("user wins")
        print("-------------------------------------------------")
        user_score = user_score + 1 
        com_lives = com_lives - 1
    
